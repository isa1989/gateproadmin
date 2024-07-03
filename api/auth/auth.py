import jwt
from datetime import datetime, timezone
from django.conf import settings
from customer.models import CustomerToken, OTP, Customer
from rest_framework.exceptions import NotFound, AuthenticationFailed
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
        phone_number=phone_number,
        defaults={"token": token_string, "issued_at": now},
    )
    return token_string


def get_phone_number_from_token(token):
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        phone_number = decoded_token["phone_number"]
        return phone_number
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.InvalidTokenError:
        # Invalid token
        return None


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


def get_customer_from_token(token):
    try:
        # Decode the JWT token
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

        # Extract the phone number from the decoded token payload
        phone_number = decoded_token.get("phone_number")

        # Retrieve the customer based on the phone number
        customer = Customer.objects.get(phone_number=phone_number)
        if not customer.is_active:
            raise AuthenticationFailed("User deleted from the system")

        return customer
    except jwt.ExpiredSignatureError:
        # Handle token expiration
        raise AuthenticationFailed("Token has expired")
    except jwt.InvalidTokenError:
        # Handle invalid token
        raise AuthenticationFailed("Invalid token")
    except Customer.DoesNotExist:
        # Handle customer not found
        raise AuthenticationFailed("Customer not found")
