from rest_framework import serializers
from notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    userId = serializers.ReadOnlyField(
        source="customer.id"
    )  # Assuming customer.id corresponds to userId
    title = serializers.SerializerMethodField()
    message = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.event.title if obj.event else None

    def get_message(self, obj):
        return obj.event.message if obj.event else None

    class Meta:
        model = Notification
        fields = ["id", "title", "message", "timestamp", "isRead", "userId"]
