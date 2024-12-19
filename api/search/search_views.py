import os
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import faiss
import numpy as np
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status, permissions
from tqdm import tqdm
import logging
from dotenv import load_dotenv

from api.models import Product, ProductImage, Category
from api.product.product_serializers import ProductSerializer

import google.generativeai as genai
import requests

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Constants
IMAGE_FOLDER = os.path.join(settings.MEDIA_ROOT, 'product_images')
TOP_K = 5
SIMILARITY_THRESHOLD = 0.7  # Ngưỡng độ tương đồng

# Device configuration
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Thiết bị sử dụng: {device}")

# Google Generative AI configuration
GOOGLE_API_KEY = "..."
if not GOOGLE_API_KEY:
    raise ValueError("Google API Key not found.")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# Load ResNet-50 model for feature extraction
print("Tải mô hình ResNet-50 cho feature extraction...")
from torchvision.models import ResNet50_Weights
resnet = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
resnet = torch.nn.Sequential(*list(resnet.children())[:-1]).to(device).eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Load images and create FAISS index
def load_images(image_folder):
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')
    return [os.path.join(image_folder, fname) for fname in os.listdir(image_folder) if fname.lower().endswith(supported_formats)]

def preprocess_images(image_paths):
    images, valid_paths = [], []
    for path in tqdm(image_paths, desc="Preprocessing images"):
        try:
            image = Image.open(path).convert('RGB')
            tensor = transform(image).unsqueeze(0).to(device)
            images.append(tensor)
            valid_paths.append(path)
        except Exception as e:
            print(f"Error processing image {path}: {e}")
    return torch.cat(images, dim=0) if images else None, valid_paths

image_paths = load_images(IMAGE_FOLDER)
images, valid_image_paths = preprocess_images(image_paths)

if images is not None:
    with torch.no_grad():
        embeddings = resnet(images).squeeze().cpu().numpy()
    embeddings /= np.linalg.norm(embeddings, axis=1, keepdims=True)
    faiss_index = faiss.IndexFlatIP(embeddings.shape[1])
    faiss_index.add(embeddings)
else:
    faiss_index = None

# Google API Classification
def classify_image_google(image_path):
    try:
        sample_file = genai.upload_file(path=image_path, display_name="Uploaded Image")
        prompt = "Analyze the object in the provided image and determine its main category. The possible categories are exclusively: Trouser, Watch, Hoodie, Clothing, Shoes, Bags, and Unknown. If the object does not fit into any of the first six categories, it must be classified as Unknown. Please respond with only the category name as a single word, without any additional explanation or text. "
        response = model.generate_content([prompt, sample_file.uri])
        return response.text.strip()
    except Exception as e:
        print(f"Google API Error: {e}")
        return "Unknown"

# ImageSearchView Class
class ImageSearchView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        if 'image' not in request.FILES:
            return JsonResponse({"detail": "No image file provided."}, status=status.HTTP_400_BAD_REQUEST)

        query_image = request.FILES['image']
        try:
            image = Image.open(query_image).convert('RGB')
            temp_image_path = os.path.join(settings.MEDIA_ROOT, 'temp_query_image.jpg')
            image.save(temp_image_path)
        except Exception as e:
            return JsonResponse({"detail": f"Invalid image file: {e}"}, status=status.HTTP_400_BAD_REQUEST)

        # Step 1: Classify image with Google API
        category = classify_image_google(temp_image_path)
        os.remove(temp_image_path)  # Remove temp image
        print(f"Predicted category: {category}")

        # Step 2: Search similar images with FAISS
        with torch.no_grad():
            query_tensor = transform(image).unsqueeze(0).to(device)
            query_embedding = resnet(query_tensor).squeeze().cpu().numpy()
            query_embedding /= np.linalg.norm(query_embedding)

        distances, indices = faiss_index.search(np.expand_dims(query_embedding, axis=0), TOP_K)
        similar_paths = [
            valid_image_paths[idx] for idx, dist in zip(indices[0], distances[0]) if dist >= SIMILARITY_THRESHOLD
        ]

        if not similar_paths:
            return JsonResponse({"category": "UNKNOWN", "products": []}, status=status.HTTP_200_OK)

        # Step 3: Find most common category and filter results
        product_counts = {}
        products = []
        for path in similar_paths:
            try:
                relative_path = os.path.relpath(path, settings.MEDIA_ROOT)
                product_image = ProductImage.objects.get(image=relative_path)
                product = product_image.product
                if product.category:
                    cat = product.category.name
                    product_counts[cat] = product_counts.get(cat, 0) + 1
                    products.append(product)
            except (ProductImage.DoesNotExist, Product.DoesNotExist):
                continue

        if not product_counts:
            return JsonResponse({"category": "UNKNOWN", "products": []}, status=status.HTTP_200_OK)

        most_common_category = max(product_counts, key=product_counts.get)
        filtered_products = [prod for prod in products if prod.category.name == most_common_category]

        serializer = ProductSerializer(filtered_products, many=True, context={'request': request})
        return JsonResponse({"category": most_common_category, "products": serializer.data}, status=status.HTTP_200_OK)