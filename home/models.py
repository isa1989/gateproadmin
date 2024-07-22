from django.db import models


class HomePage(models.Model):
    logo = models.ImageField(upload_to="homepage/", blank=True, null=True)
    banner_image = models.ImageField(upload_to="homepage/", blank=True, null=True)
    feature_image = models.ImageField(upload_to="homepage/", blank=True, null=True)


class ScreenFrame(models.Model):
    image = models.ImageField(upload_to="homepage/", blank=True, null=True)


class MobileMockup(models.Model):
    image = models.ImageField(upload_to="homepage/", blank=True, null=True)
