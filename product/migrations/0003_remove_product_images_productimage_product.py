# Generated by Django 5.0.6 on 2024-06-11 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_rename_images_backend_product_images_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="images",
        ),
        migrations.AddField(
            model_name="productimage",
            name="product",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="product.product",
            ),
            preserve_default=False,
        ),
    ]
