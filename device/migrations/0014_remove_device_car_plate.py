# Generated by Django 5.0.6 on 2024-07-02 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("device", "0013_device_car_plate"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="device",
            name="car_plate",
        ),
    ]