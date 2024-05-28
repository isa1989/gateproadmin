from rest_framework import serializers
from ..models import Settings

class SettingsSerializer(serializers.ModelSerializer):
    banner_image = serializers.SerializerMethodField()

    class Meta:
        model = Settings
        fields = ['banner_image']

    def get_banner_image(self, obj):
        request = self.context.get('request')
        if obj.banner_image and request:
            return request.build_absolute_uri(obj.banner_image.url)
        return None
