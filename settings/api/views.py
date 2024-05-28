from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import Settings
from .serializers import SettingsSerializer

class SettingsViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def banner_image(self, request):
        settings = Settings.get_solo()
        serializer = SettingsSerializer(settings, context={'request': request})
        return Response(serializer.data)
