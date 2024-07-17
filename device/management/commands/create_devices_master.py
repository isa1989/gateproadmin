import random
from django.core.management.base import BaseCommand
from device.models import Device


class Command(BaseCommand):
    help = "Adds devices sequentially"

    def handle(self, *args, **options):
        start_number = 393000001
        end_number = 393001001
        device_count = 0
        for number in range(start_number, end_number):
            device = Device.objects.create(
                deviceNumber=number, deviceName=number, device_type="master"
            )
            device_count += 1

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {device_count} devices"),
        )
