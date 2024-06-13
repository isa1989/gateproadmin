# serializers.py
from rest_framework import serializers
from customer.models import Customer, OTP


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=12)
    name = serializers.CharField(max_length=200, required=False)
    surname = serializers.CharField(max_length=200, required=False)

    class Meta:
        model = Customer
        fields = [
            "phone_number",
            "name",
            "surname",
        ]

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
