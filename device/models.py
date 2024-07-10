import qrcode
from django.db import models
from customer.models import Customer
from django.db import models
from django.conf import settings
from django.core.files.base import ContentFile
from io import BytesIO


class Device(models.Model):
    STATUS_CHOICES = [
        ("online", "Online"),
        ("offline", "Offline"),
    ]
    TYPE_CHOICES = [
        ("juno", "Juno"),
        ("master", "Master"),
    ]
    owner = models.ForeignKey(
        Customer,
        related_name="owned_device",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    members = models.ManyToManyField(Customer, related_name="devices", blank=True)
    deviceNumber = models.CharField(max_length=200, blank=True, null=True, unique=True)
    deviceName = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    device_type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, blank=True, null=True
    )
    qr_code = models.ImageField(upload_to="qrcodes/", blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate QR code when saving the object
        if not self.qr_code:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.deviceNumber)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            # Save QR code image to a BytesIO buffer
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            filename = f"qr_{self.deviceNumber}.png"

            # Create a Django ContentFile from the buffer
            self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.deviceNumber


class Pin(models.Model):
    STATUS_CHOICES = [
        ("on", "On"),
        ("off", "Off"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="off")
    device = models.OneToOneField(Device, related_name="pin", on_delete=models.CASCADE)

    def __str__(self):
        return f"Pin {self.id}"


class CarPlate(models.Model):
    carPlateNumber = models.CharField(max_length=20, unique=True)
    carName = models.CharField(max_length=20)

    def __str__(self):
        return self.carPlateNumber
