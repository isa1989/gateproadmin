import random
from django.core.management.base import BaseCommand
from device.models import Device, Pin


class Command(BaseCommand):
    help = "Creates random Device instances"

    def handle(self, *args, **kwargs):
        start_number = 383000001
        end_number = 393000001
        num_devices = 1000

        for _ in range(num_devices):
            device_number = random.randint(start_number, end_number)
            device_name = str(device_number)

            device = Device.objects.create(
                deviceNumber=device_number,
                deviceName=device_name,
            )
            Pin.objects.create(device=device)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {num_devices} devices"),
        )
