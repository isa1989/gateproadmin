# Generated by Django 5.0.6 on 2024-06-27 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0003_alter_settings_banner_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="settings",
            name="smscenter_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]