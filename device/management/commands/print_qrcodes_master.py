from django.core.management.base import BaseCommand
from device.models import Device  # Change this to the correct import path
import qrcode
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = "Prints all QR codes for devices on A4 pages"

    def handle(self, *args, **options):
        # A4 dimensions in pixels (assuming 300 DPI)
        A4_WIDTH = 2480  # 8.27 inches * 300 DPI = 2480 pixels
        A4_HEIGHT = 3508  # 11.69 inches * 300 DPI = 3508 pixels

        # Margin and spacing between QR codes
        MARGIN = 40  # Pixels
        QR_SIZE = 290  # Size of each QR code in pixels
        SPACING = 45  # Space between QR codes in pixels

        # Get all QR codes
        qr_codes = Device.objects.filter(device_type="master")

        # Total number of QR codes
        total_qr_count = qr_codes.count()

        # Calculate the number of pages
        qr_per_page = int((A4_WIDTH - 2 * MARGIN) // (QR_SIZE + SPACING)) * int(
            (A4_HEIGHT - 2 * MARGIN) // (QR_SIZE + SPACING)
        )
        page_count = (
            total_qr_count + qr_per_page - 1
        ) // qr_per_page  # Ceiling division

        # Create A4 pages
        for page_num in range(page_count):
            page = Image.new("RGB", (A4_WIDTH, A4_HEIGHT), "white")
            draw = ImageDraw.Draw(page)

            # Font settings (optional)
            font_size = 36
            font = ImageFont.truetype("arial.ttf", font_size)

            # Get QR codes for the current page
            qr_start = page_num * qr_per_page
            qr_end = min(qr_start + qr_per_page, total_qr_count)
            qr_codes_page = qr_codes[qr_start:qr_end]

            # Place QR codes on the A4 page
            x, y = MARGIN, MARGIN
            for device in qr_codes_page:
                # Generate QR code if not already generated
                if not device.qr_code:
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
                    qr.add_data(device.deviceNumber)
                    qr.make(fit=True)

                    img = qr.make_image(fill_color="black", back_color="white")

                    # Save QR code to a BytesIO buffer
                    buffer = BytesIO()
                    img.save(buffer, format="PNG")
                    filename = f"qr_{device.deviceNumber}.png"

                    # Save the BytesIO buffer as a Django ContentFile
                    device.qr_code.save(
                        filename, ContentFile(buffer.getvalue()), save=False
                    )

                # Place QR code on the A4 page
                qr_img = Image.open(device.qr_code)
                qr_img = qr_img.resize(
                    (QR_SIZE, QR_SIZE), Image.LANCZOS
                )  # Use Image.LANCZOS for high-quality resizing
                page.paste(qr_img, (x, y))

                # Optionally write the device number below the QR code
                draw.text(
                    (x + 30, y + QR_SIZE + 3),
                    device.deviceNumber,
                    fill="black",
                    font=font,
                )

                # Move to the next position
                x += QR_SIZE + SPACING

                # Move to a new row if at the end of a column
                if x > A4_WIDTH - QR_SIZE - MARGIN:
                    x = MARGIN
                    y += QR_SIZE + SPACING

            # Save or display the A4 page
            page.save(f"output_page_{page_num + 1}.png")

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully printed {total_qr_count} QR codes on {page_count} A4 pages"
            )
        )
