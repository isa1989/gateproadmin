# Generated by Django 5.0.6 on 2024-07-30 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_homepage_instagram_homepage_whatsapp"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="app_store",
            field=models.URLField(blank=True, null=True, verbose_name="App Store URL"),
        ),
        migrations.AddField(
            model_name="homepage",
            name="play_store",
            field=models.URLField(blank=True, null=True, verbose_name="Play Store URL"),
        ),
    ]
