from django.db import models
from customer.models import Customer


class Device(models.Model):
    STATUS_CHOICES = [
        ("online", "Online"),
        ("offline", "Offline"),
    ]
    owner = models.ForeignKey(
        Customer,
        related_name="owned_device",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    members = models.ManyToManyField(Customer, related_name="devices", blank=True)
    deviceNumber = models.CharField(max_length=200, blank=True, null=True)
    deviceName = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.deviceName


class Pin(models.Model):
    STATUS_CHOICES = [
        ("on", "On"),
        ("off", "Off"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="off")
    device = models.OneToOneField(Device, related_name="pin", on_delete=models.CASCADE)

    def __str__(self):
        return f"Pin {self.id}"
