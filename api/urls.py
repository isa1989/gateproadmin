# api/urls.py
from django.urls import path
from api.views import (
    CustomerPhoneRegistrationView,
    CustomerProfileEditView,
    CustomerPhoneLoginView,
    CustomerLogoutView,
    CustomerDeleteView,
    CustomerPhoneVerifyOtpView,
)

urlpatterns = [
    path(
        "v1/register/",
        CustomerPhoneRegistrationView.as_view(),
        name="customer_phone_registration",
    ),
    path("v1/login/", CustomerPhoneLoginView.as_view(), name="customer_phone_login"),
    path(
        "v1/verify-otp/",
        CustomerPhoneVerifyOtpView.as_view(),
        name="customer-verify-otp",
    ),
    path("logout/", CustomerLogoutView.as_view(), name="customer_logout"),
    path(
        "customer/profile/edit/<int:pk>/",
        CustomerProfileEditView.as_view(),
        name="customer_profile_edit",
    ),
    path("customer/delete/", CustomerDeleteView.as_view(), name="customer_delete"),
]
