import jwt
from datetime import datetime, timezone
from django.conf import settings
from customer.models import CustomerToken, OTP
from rest_framework.exceptions import NotFound
from django.utils import timezone


def generate_or_update_jwt_token(phone_number):
    # Create the token payload without an expiration date
    now = timezone.now().isoformat()
    token_payload = {"phone_number": phone_number, "issued_at": now}
    token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm="HS256")
    # Convert byte string to regular string
    token_string = token.decode("utf-8") if isinstance(token, bytes) else token
    # Save or update the token instance
    token_instance, _ = CustomerToken.objects.update_or_create(
        phone_number=phone_number, defaults={"token": token_string}
    )
    return token_string


def verify_jwt_token(token, phone_number):
    try:
        # Check if the token exists in the database
        token_obj = CustomerToken.objects.get(token=token, phone_number=phone_number)
        # Token exists and is valid
        return True
    except CustomerToken.DoesNotExist:
        # Token does not exist in the database
        return False


def validate_otp_and_generate_token(otp_code, customer_id):
    try:
        otp_instance = OTP.objects.get(otp_code=otp_code)
    except OTP.DoesNotExist:
        raise NotFound("Invalid OTP code.")

    if otp_instance.customer.id != customer_id:
        raise NotFound("Invalid OTP code.")

    customer_instance = otp_instance.customer
    token = generate_or_update_jwt_token(customer_instance)
    return {"customer_id": customer_instance.id, "token": token}