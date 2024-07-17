from django.contrib import admin
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from device.models import Device, CarPlate


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("deviceNumber", "deviceName", "status", "device_type")
    list_filter = ("status", "device_type")
    search_fields = ("deviceNumber", "deviceName")

    # Özel aksiyon fonksiyonunu tanımlayın
    def export_device_numbers_to_txt(self, request, queryset):
        response = HttpResponse(content_type="text/plain")
        response["Content-Disposition"] = 'attachment; filename="device_numbers.txt"'

        # Seçilen cihaz numaralarını txt dosyasına yazın
        device_numbers = queryset.values_list("deviceNumber", flat=True)
        device_numbers_txt = "\n".join(device_numbers)

        response.write(device_numbers_txt)
        return response

    # Admin paneline aksiyon düğmesini ekleyin
    export_device_numbers_to_txt.short_description = "Export Device Numbers to TXT"
    actions = [export_device_numbers_to_txt]


admin.site.register(CarPlate)
