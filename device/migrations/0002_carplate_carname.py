# Generated by Django 5.0.6 on 2024-07-08 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("device", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="carplate",
            name="carName",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]