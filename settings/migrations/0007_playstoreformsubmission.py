# Generated by Django 5.0.6 on 2024-07-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0006_remove_settings_sms_private_key_and_more"),
    ]

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
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]