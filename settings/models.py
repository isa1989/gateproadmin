from django.db import models
from solo.models import SingletonModel
from ckeditor.fields import RichTextField


class Settings(SingletonModel):
    banner_image = models.ImageField(upload_to="banner-img")


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
