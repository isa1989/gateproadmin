# serializers.py
from rest_framework import serializers
from faq.models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ["id", "question", "answer", "helpful_count", "not_helpful_count"]
