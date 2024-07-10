from django.contrib import admin
from device.models import Device, Pin, CarPlate


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("deviceNumber", "deviceName", "status", "device_type")
    list_filter = ("status", "device_type")
    search_fields = ("deviceNumber", "deviceName")


admin.site.register(Pin)
admin.site.register(CarPlate)
