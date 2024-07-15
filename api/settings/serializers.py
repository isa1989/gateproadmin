# serializers.py
from rest_framework import serializers
from settings.models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            "telegram",
            "website",
            "instagram",
            "facebook",
            "whatsapp",
            "phoneNumber",
        )
