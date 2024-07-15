from django.db import models
from solo.models import SingletonModel
from ckeditor.fields import RichTextField


class Settings(SingletonModel):
    banner_image = models.ImageField(upload_to="banner-img")
    smscenter_pbk = models.CharField(
        max_length=500, blank=True, verbose_name="Public key"
    )
    smscenter_pvk = models.CharField(
        max_length=500, blank=True, verbose_name="Private key"
    )
    smscenter_url = models.CharField(max_length=500, blank=False, verbose_name="SmSURL")
    smscenter_username = models.CharField(
        max_length=500, blank=False, verbose_name="Username"
    )


class PlayStoreFormSubmission(models.Model):
    number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    reason = models.CharField(
        max_length=50,
        choices=[
            ("privacy", "Privacy concerns"),
            ("no_longer_using", "No longer using the service"),
            ("different_app", "Prefer a different app"),
            ("hacked", "Account hacked or compromised"),
            ("notifications", "Too many notifications/emails"),
            ("other", "Other (please specify)"),
        ],
    )
    other_reason = models.CharField(max_length=255, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Form Submission {self.id}"


class PrivacyPolicy(models.Model):
    content = RichTextField()

    def __str__(self):
        return "Privacy Policy"


class TermsConditions(models.Model):
    content = RichTextField()

    def __str__(self):
        return "Terms & Conditions"


class ContactUs(models.Model):
    telegram = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = "ContactUs"
        verbose_name_plural = "ContactUs"
