# serializers.py
from rest_framework import serializers
from customer.models import Customer


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=12)
    first_name = serializers.CharField(max_length=200, required=False)
    last_name = serializers.CharField(max_length=200, required=False)
    register_completed = serializers.BooleanField(required=False)

    class Meta:
        model = Customer
        fields = ['phone_number', 'first_name', 'last_name', 'register_completed']

    def validate_phone_number(self, value):
        # Check if the phone number starts with "+994"
        if not value.startswith("994"):
            raise serializers.ValidationError("Phone number must start with 994.")
        # Implement OTP validation logic here
        # Assuming OTP validation is successful
        return value

    # def create(self, validated_data):
    #     return Customer.objects.create_user(phone_number=validated_data['phone_number'])
