# views.py

from rest_framework import generics, status
from django.http import Http404, JsonResponse
from rest_framework.response import Response
from django.db.models import Q
from device.models import Device
from api.auth.auth import get_customer_from_token
from .serializers import DeviceSerializer, PinSerializer, InviteMemberSerializer
from api.permissions import IsCustomerAuthenticated, IsOwnerOfDevice
from device.models import Pin
from rest_framework.views import APIView


class DeviceListView(generics.ListAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsCustomerAuthenticated]
    queryset = Device.objects.all()

    def get_queryset(self):
        token = self.request.headers.get("Authorization")
        customer = get_customer_from_token(token)
        queryset = Device.objects.filter(
            Q(owner=customer) | Q(members=customer)
        ).distinct()
        return queryset


class DeviceDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsCustomerAuthenticated]
    queryset = Device.objects.all()
    lookup_field = "pk"

    def get_queryset(self):
        token = self.request.headers.get("Authorization")
        customer = get_customer_from_token(token)
        queryset = Device.objects.filter(
            Q(owner=customer) | Q(members=customer)
        ).distinct()
        return queryset

    def get_permissions(self):
        if self.request.method == "DELETE":
            self.permission_classes = [IsCustomerAuthenticated, IsOwnerOfDevice]
        return super(DeviceDetailView, self).get_permissions()

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Device.DoesNotExist:
            return Response(
                {"message": "Device not found."}, status=status.HTTP_404_NOT_FOUND
            )

        return Response({"message": "Device unlinked successfully."})

    def perform_destroy(self, instance):
        # Custom logic to unlink the device from the authenticated user
        instance.owner = None  # Assuming owner is a ForeignKey to the user
        instance.save()


class DevicePinDetailAPIView(generics.UpdateAPIView):
    serializer_class = PinSerializer
    permission_classes = [IsCustomerAuthenticated]
    queryset = Pin.objects.all()
    lookup_url_kwarg = "pin_id"

    def patch(self, request, *args, **kwargs):
        try:
            pin = self.get_object()
        except Pin.DoesNotExist:
            return Response(
                {"message": "Pin not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance=pin, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Pin status updated successfully."})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InviteMemberAPIView(generics.CreateAPIView):
    serializer_class = InviteMemberSerializer
    permission_classes = [IsCustomerAuthenticated, IsOwnerOfDevice]

    def post(self, request, deviceId, *args, **kwargs):
        token = self.request.headers.get("Authorization")
        customer = get_customer_from_token(
            token
        )  # Assuming this function retrieves the customer from token

        try:
            device = Device.objects.get(id=deviceId, owner=customer)
        except Device.DoesNotExist:
            return Response(
                {"message": "Device not found or you are not the owner."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            phoneNumber = serializer.validated_data.get("phoneNumber")

            # Implement your logic to send invitation to phoneNumber here
            # For example, you might send an SMS or email invitation

            return Response({"message": "Invitation sent successfully."})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveMemberFromDeviceAPIView(generics.DestroyAPIView):
    permission_classes = [IsCustomerAuthenticated, IsOwnerOfDevice]
    # queryset = Device.objects.all()

    def delete(self, request, *args, **kwargs):
        token = self.request.headers.get("Authorization")
        customer = get_customer_from_token(token)

        try:
            device = Device.objects.get(id=kwargs["deviceId"], owner=customer)
        except Device.DoesNotExist:
            return Response(
                {"message": "Device not found or you are not the owner."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Check if the memberId exists in members of the device
        if device.members.filter(id=kwargs["memberId"]).exists():
            device.members.remove(kwargs["memberId"])
            return Response({"message": "Member removed successfully."})
        else:
            return JsonResponse(
                {"message": "Member not found in device."},
                status=status.HTTP_404_NOT_FOUND,
            )
