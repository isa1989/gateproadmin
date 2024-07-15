# views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny
from settings.models import ContactUs
from .serializers import ContactUsSerializer


class ContactUsListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
