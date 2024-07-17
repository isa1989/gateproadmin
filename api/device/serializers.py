# serializers.py

from rest_framework import serializers
from device.models import Device, CarPlate
from api.auth.auth import get_customer_from_token
from customer.models import Customer
from django.core.validators import RegexValidator


class MemberSerializer(serializers.ModelSerializer):
    memberId = serializers.IntegerField(source="id", read_only=True)
    phoneNumber = serializers.CharField(source="phone_number")
    name = serializers.CharField()

    class Meta:
        model = Customer
        fields = ("memberId", "phoneNumber", "name")


class DeviceSerializer(serializers.ModelSerializer):
    deviceId = serializers.IntegerField(source="id", read_only=True)
    isOwner = serializers.SerializerMethodField()
    members = MemberSerializer(many=True, required=False)
    status = serializers.CharField(required=False)
    state = serializers.SerializerMethodField()

    class Meta:
        model = Device
        fields = (
            "deviceId",
            "owner",
            "deviceNumber",
            "deviceName",
            "status",
            "state",
            "isOwner",
            "members",
        )

    def get_isOwner(self, obj):
        request = self.context.get("request")
        if request is None:
            return False
        token = request.headers.get("Authorization")
        customer = get_customer_from_token(
            token
        )  # Assuming this function retrieves Customer from token
        return customer == obj.owner if obj.owner else False

    def get_state(self, obj):
        # Determine state based on mqtt_response value
        mqtt_response = self.context.get("mqtt_response")
        if mqtt_response == "0":
            return "on"
        elif mqtt_response == "1":
            return "off"
        else:
            return None


class InviteMemberSerializer(serializers.Serializer):
    phoneNumber = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r"^994\d{9}$",  # Regex pattern for phone numbers starting with 994 and total 12 digits
                message="Phone number must start with 994 and have 12 digits",
                code="invalid_phone_number",
            )
        ]
    )

    def validate_phoneNumber(self, value):
        if not value.startswith("994"):
            raise serializers.ValidationError("Phone number must start with 994.")
        return value


class CarPlateSerializer(serializers.ModelSerializer):
    carPlateId = serializers.IntegerField(source="id", read_only=True)

    class Meta:
        model = CarPlate
        fields = ["carPlateId", "carPlateNumber", "carName"]
