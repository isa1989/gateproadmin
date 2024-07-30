from django.db import models


class HomePage(models.Model):
    logo = models.ImageField(upload_to="homepage/", blank=True, null=True)
    banner_image = models.ImageField(upload_to="homepage/", blank=True, null=True)
    feature_image = models.ImageField(upload_to="homepage/", blank=True, null=True)
    whatsapp = models.URLField(
        blank=True, null=True, help_text="Enter your WhatsApp URL"
    )
    instagram = models.URLField(
        blank=True, null=True, help_text="Enter your Instagram URL"
    )
    app_store = models.URLField(blank=True, null=True, verbose_name="App Store URL")
    play_store = models.URLField(blank=True, null=True, verbose_name="Play Store URL")


class ScreenFrame(models.Model):
    image = models.ImageField(upload_to="homepage/", blank=True, null=True)


class MobileMockup(models.Model):
    image = models.ImageField(upload_to="homepage/", blank=True, null=True)
