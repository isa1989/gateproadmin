# serializers.py

from rest_framework import serializers
from device.models import Device, Pin

# from api.auth.serializers import (
#     CustomerSerializer,
# )
from api.auth.auth import get_customer_from_token
from customer.models import Customer


class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = ("id", "status")


class MemberSerializer(serializers.ModelSerializer):
    memberId = serializers.IntegerField(source="id")
    phoneNumber = serializers.CharField(source="phone_number")
    name = serializers.CharField()

    class Meta:
        model = Customer
        fields = ("memberId", "phoneNumber", "name")


class DeviceSerializer(serializers.ModelSerializer):
    deviceId = serializers.IntegerField(source="id")
    # owner = CustomerSerializer(
    #     id
    # )  # Assuming CustomerSerializer is defined and imported correctly
    members = MemberSerializer(
        many=True
    )  # Assuming CustomerSerializer is defined and imported correctly
    pin = PinSerializer()
    isOwner = serializers.SerializerMethodField()

    class Meta:
        model = Device
        fields = (
            "deviceId",
            "deviceName",
            "status",
            "isOwner",
            "members",
            "pin",
        )

    def get_isOwner(self, obj):
        request = self.context.get("request")
        token = request.headers.get("Authorization")
        customer = get_customer_from_token(token)
        return customer == obj.owner if obj.owner else False
