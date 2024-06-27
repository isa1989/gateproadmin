# views.py

from rest_framework import generics
from device.models import Device
from .serializers import DeviceSerializer
from api.permissions import IsCustomerAuthenticated


class DeviceListView(generics.ListAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsCustomerAuthenticated]
    queryset = Device.objects.all()


class DeviceDetailView(generics.RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = "pk"
