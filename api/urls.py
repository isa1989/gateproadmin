# api/urls.py
from django.urls import path
from .views import CustomerPhoneRegistrationView

urlpatterns = [
    path('register/', CustomerPhoneRegistrationView.as_view(), name='customer_phone_registration'),
    # path('verify/', OTPVerificationView.as_view(), name='otp_verification'),
    # Add more URL patterns as needed for other API views
]
