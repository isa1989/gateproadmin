# Generated by Django 5.0.6 on 2024-06-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0002_settings_sms_private_key_settings_sms_public_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="settings",
            name="banner_image",
            field=models.ImageField(blank=True, null=True, upload_to="banner-img"),
        ),
        migrations.AlterField(
            model_name="settings",
            name="sms_private_key",
            field=models.CharField(
                blank=True, max_length=500, null=True, verbose_name="Private key"
            ),
        ),
        migrations.AlterField(
            model_name="settings",
            name="sms_public_key",
            field=models.CharField(
                blank=True, max_length=500, null=True, verbose_name="Public key"
            ),
        ),
    ]
