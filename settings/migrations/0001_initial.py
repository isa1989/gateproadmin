# Generated by Django 5.0.6 on 2024-07-10 13:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PlayStoreFormSubmission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=20)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "reason",
                    models.CharField(
                        choices=[
                            ("privacy", "Privacy concerns"),
                            ("no_longer_using", "No longer using the service"),
                            ("different_app", "Prefer a different app"),
                            ("hacked", "Account hacked or compromised"),
                            ("notifications", "Too many notifications/emails"),
                            ("other", "Other (please specify)"),
                        ],
                        max_length=50,
                    ),
                ),
                ("other_reason", models.CharField(blank=True, max_length=255)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="PrivacyPolicy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", ckeditor.fields.RichTextField()),
                ("content_az", ckeditor.fields.RichTextField(null=True)),
                ("content_en", ckeditor.fields.RichTextField(null=True)),
                ("content_ru", ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("banner_image", models.ImageField(upload_to="banner-img")),
                (
                    "smscenter_pbk",
                    models.CharField(
                        blank=True, max_length=500, verbose_name="Public key"
                    ),
                ),
                (
                    "smscenter_pvk",
                    models.CharField(
                        blank=True, max_length=500, verbose_name="Private key"
                    ),
                ),
                (
                    "smscenter_url",
                    models.CharField(max_length=500, verbose_name="SmSURL"),
                ),
                (
                    "smscenter_username",
                    models.CharField(max_length=500, verbose_name="Username"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TermsConditions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", ckeditor.fields.RichTextField()),
                ("content_az", ckeditor.fields.RichTextField(null=True)),
                ("content_en", ckeditor.fields.RichTextField(null=True)),
                ("content_ru", ckeditor.fields.RichTextField(null=True)),
            ],
        ),
    ]
