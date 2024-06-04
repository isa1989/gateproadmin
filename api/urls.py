# api/urls.py
from django.urls import path
from api.views import CustomerPhoneRegistrationView, CustomerProfileEditView, CustomerPhoneLoginView, CustomerLogoutView, CustomerDeleteView

urlpatterns = [
    path('register/', CustomerPhoneRegistrationView.as_view(), name='customer_phone_registration'),
    path('login/', CustomerPhoneLoginView.as_view(), name='customer_phone_login'),
     path('logout/', CustomerLogoutView.as_view(), name='customer_logout'),
    path('customer/profile/edit/<int:pk>/', CustomerProfileEditView.as_view(), name='customer_profile_edit'),
    path('customer/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
]
