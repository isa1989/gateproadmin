from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from notification.models import Notification
from api.permissions import IsCustomerAuthenticated
from .serializers import NotificationSerializer
from api.auth.auth import get_customer_from_token
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsCustomerAuthenticated]

    def get_queryset(self):
        token = self.request.headers.get("Authorization")
        customer = get_customer_from_token(token)

        return Notification.objects.filter(customer=customer)


class NotificationDetailView(generics.RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsCustomerAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if "read" in request.query_params and request.query_params["read"] == "true":
            instance.isRead = True
            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UnreadNotificationCountView(generics.GenericAPIView):
    permission_classes = [IsCustomerAuthenticated]

    def get(self, request, *args, **kwargs):
        token = self.request.headers.get("Authorization")
        customer = get_customer_from_token(token)
        unread_count = Notification.objects.filter(
            customer=customer, isRead=False
        ).count()
        return Response({"unreadCount": unread_count})


class MarkAllNotificationsAsReadView(APIView):
    permission_classes = [IsCustomerAuthenticated]

    def post(self, request):
        token = request.headers.get("Authorization")
        customer = get_customer_from_token(token)
        Notification.objects.filter(customer=customer, isRead=False).update(isRead=True)
        return Response({"message": "All notifications marked as read."})
