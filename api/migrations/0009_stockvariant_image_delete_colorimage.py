# Generated by Django 5.1.1 on 2024-12-17 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_stockvariant_image_colorimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockvariant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='variant_images/'),
        ),
        migrations.DeleteModel(
            name='ColorImage',
        ),
    ]
