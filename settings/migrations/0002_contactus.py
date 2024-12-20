# Generated by Django 5.0.6 on 2024-07-15 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactUs",
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
                ("telegram", models.URLField(blank=True, null=True)),
                ("website", models.URLField(blank=True, null=True)),
                ("instagram", models.URLField(blank=True, null=True)),
                ("facebook", models.URLField(blank=True, null=True)),
                ("whatsapp", models.CharField(blank=True, max_length=15, null=True)),
                ("phoneNumber", models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
