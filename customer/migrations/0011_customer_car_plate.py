# Generated by Django 5.0.6 on 2024-07-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0010_remove_customer_preferred_language"),
        ("device", "0014_remove_device_car_plate"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="car_plate",
            field=models.ManyToManyField(
                blank=True, related_name="customer_cars", to="device.carplate"
            ),
        ),
    ]