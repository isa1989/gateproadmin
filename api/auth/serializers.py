# serializers.py
from rest_framework import serializers
from customer.models import Customer, OTP


class OTPSerializer(serializers.ModelSerializer):
    def validate_phone_number(self, value):
        """
        Check if the phone number has exactly 12 characters.
        """
        if len(value) != 12:
            raise serializers.ValidationError(
                "Phone number must be exactly 12 characters long."
            )
        return value

    class Meta:
        model = OTP
        fields = ["phone_number", "otp_code"]


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=12)
    name = serializers.CharField(max_length=200, required=False)
    surname = serializers.CharField(max_length=200, required=False)

    class Meta:
        model = Customer
        fields = ["phone_number", "name", "surname"]

    def validate_phone_number(self, value):
        # Check if the phone number starts with "+994"
        if not value.startswith("994"):
            raise serializers.ValidationError("Phone number must start with 994.")
        # Implement OTP validation logic here
        # Assuming OTP validation is successful
        return value


class CustomerLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=12)

    class Meta:
        model = Customer
        fields = ["phone_number"]

    def validate_phone_number(self, value):
        # Check if the phone number starts with "+994"
        if not value.startswith("994"):
            raise serializers.ValidationError("Phone number must start with 994.")
        # Implement OTP validation logic here
        # Assuming OTP validation is successful
        return value


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "name",
            "surname",
            "phone_number",
            "firebase_token",
            "email",
            "email_address",
            "sms",
            "push",
            "is_active",
        ]

        extra_kwargs = {
            "email": {"required": False},
            "sms": {"required": False},
            "push": {"required": False},
        }
