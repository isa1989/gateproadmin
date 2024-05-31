from django.contrib import admin
from .models import Customer, OTP, CustomerToken

# Register your models here.

admin.site.register(Customer)
admin.site.register(OTP)
admin.site.register(CustomerToken)