# Generated by Django 5.1.1 on 2024-12-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_product_sku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockvariant',
            name='image',
        ),
        migrations.AddField(
            model_name='productimage',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
