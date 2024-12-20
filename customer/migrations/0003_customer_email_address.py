# Generated by Django 5.0.6 on 2024-07-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="email_address",
            field=models.EmailField(
                blank=True,
                max_length=255,
                null=True,
                unique=True,
                verbose_name="Email address",
            ),
        ),
    ]
