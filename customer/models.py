from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False, verbose_name="Customer name")
    address = models.CharField(max_length=200, null=True, blank=False, verbose_name="Customer address")

    def __str__(self):
        return self.name


