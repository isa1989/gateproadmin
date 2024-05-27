from django.db import models
from customer.models import Customer

# Create your models here.

class Device(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='devices')
    ip_address = models.GenericIPAddressField(unique=True, blank=False, null=True, verbose_name="Ip address")
    device_type = models.CharField(max_length=255, blank=False, null=True, verbose_name="Device Type")
    serial_number = models.CharField(max_length=50, null=True, verbose_name="Serial Number")
    qr_code = models.ImageField(upload_to='qr_codes/', verbose_name="QR Code")

    
    def __str__(self):
        return f"{self.customer.name} - {self.ip_address}"


