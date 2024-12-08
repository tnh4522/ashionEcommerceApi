from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .product.product_serializers import ProductSerializer

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, label='Confirm Password',
                                      style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password', 'password2',
            'role', 'phone_number', 'date_of_birth', 'gender', 'profile_picture'
        )
        extra_kwargs = {'password': {'write_only': True}, 'password2': {'write_only': True},
                        'email': {'required': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        role = validated_data.pop('role', None)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', ''),
            date_of_birth=validated_data.get('date_of_birth'),
            gender=validated_data.get('gender'),
            profile_picture=validated_data.get('profile_picture')
        )
        if role:
            user.role = role
            user.save()

        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['role'] = user.role.name if user.role else None
        token['email'] = user.email
        token['id'] = user.id

        permissions = UserPermission.objects.filter(user=user).values_list('permission__model_name',
                                                                           'permission__action', 'allowed')
        token['permissions'] = [
            f"{model_name}:{action}" for model_name, action, allowed in permissions if allowed
        ]
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data.update({
            'id': self.user.id,
            'role': self.user.role.name if self.user.role else None,
            'username': self.user.username,
            'email': self.user.email,
        })

        permissions = UserPermission.objects.filter(user=self.user).values_list('permission__model_name',
                                                                                'permission__action', 'allowed')
        data['permissions'] = [
            f"{model_name}:{action}" for model_name, action, allowed in permissions if allowed
        ]
        return data


class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)
    social_links = serializers.JSONField(required=False)
    preferences = serializers.JSONField(required=False)
    role_display = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'phone_number', 'first_name', 'last_name',
            'date_of_birth', 'gender', 'profile_picture', 'bio',
            'social_links', 'preferences', 'role', 'role_display', 'is_superuser'
        )
        read_only_fields = ('id',)

    def get_role_display(self, obj):
        return obj.role.name if obj.role else None


class UserCreateSerializer(serializers.ModelSerializer):
    social_links = serializers.JSONField(required=False)
    preferences = serializers.JSONField(required=False)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'role', 'phone_number',
            'date_of_birth', 'gender', 'profile_picture',
            'first_name', 'last_name', 'bio', 'social_links', 'preferences'
        )
        extra_kwargs = {'username': {'required': True}}

    def create(self, validated_data):
        social_links = validated_data.pop('social_links', {})
        preferences = validated_data.pop('preferences', {})

        role = validated_data.get('role')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=None,
            role=validated_data.get('role'),
            phone_number=validated_data.get('phone_number', ''),
            date_of_birth=validated_data.get('date_of_birth'),
            gender=validated_data.get('gender'),
            profile_picture=validated_data.get('profile_picture'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            bio=validated_data.get('bio', ''),
            social_links=social_links,
            preferences=preferences,
        )
        user.save()

        if role:
            role_permissions = RolePermission.objects.filter(role=role, allowed=True)

            user_permissions = [
                UserPermission(user=user, permission=rp.permission, allowed=True)
                for rp in role_permissions
            ]

            UserPermission.objects.bulk_create(user_permissions)

        return user


class CreatePasswordSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, label='Confirm Password',
                                      style={'input_type': 'password'})

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')

        try:
            user = User.objects.get(username=username)
            if user and not user.has_usable_password():
                user.set_password(password)
                user.save()
                return user
            else:
                raise serializers.ValidationError({'username': "User already has a password or does not exist."})
        except User.DoesNotExist:
            raise serializers.ValidationError({'username': "Invalid username."})


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'name', 'parent', 'slug', 'description', 'image',
            'is_active', 'meta_title', 'meta_description', 'sort_order'
        )

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class UserPermissionSerializer(serializers.ModelSerializer):
    permission = PermissionSerializer(read_only=True)

    class Meta:
        model = UserPermission
        fields = ('id', 'permission', 'allowed')


class RoleSerializer(serializers.ModelSerializer):
    permissions = serializers.ListField(
        child=serializers.CharField(), write_only=True
    )
    permissions_display = serializers.SerializerMethodField()
    permissions_objects = serializers.SerializerMethodField()

    class Meta:
        model = Role
        fields = ('id', 'name', 'description', 'permissions', 'permissions_display', 'permissions_objects')

    def get_permissions_display(self, obj):
        permissions = RolePermission.objects.filter(allowed=True, role=obj)
        return [f"{perm.permission.model_name}:{perm.permission.action}" for perm in permissions]

    def get_permissions_objects(self, obj):
        role_permissions = RolePermission.objects.filter(allowed=True, role=obj)
        permissions = [rp.permission for rp in role_permissions]
        return PermissionSerializer(permissions, many=True).data

    def validate_permissions(self, value):
        permissions = []
        for perm_str in value:
            try:
                model_name, action = perm_str.split(':')
                permission = Permission.objects.get(model_name=model_name, action=action)
                permissions.append(permission)
            except (ValueError, Permission.DoesNotExist):
                raise serializers.ValidationError(f"Invalid permission: {perm_str}")
        return permissions

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', [])
        role = Role.objects.create(
            name=validated_data['name'],
            description=validated_data.get('description', '')
        )

        role_permissions = [
            RolePermission(role=role, permission=permission, allowed=True)
            for permission in permissions
        ]
        RolePermission.objects.bulk_create(role_permissions)

        return role