# Generated by Django 5.0.6 on 2024-06-27 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "device",
            "0002_pin_remove_device_customer_remove_device_device_type_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="device",
            name="isOwner",
        ),
    ]