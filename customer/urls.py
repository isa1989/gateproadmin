
from django.urls import path
from . import views

urlpatterns = [
    path('customers', views.CustomerListView.as_view(),name="customer-list"),
    path('customer/create/', views.CustomerCreate.as_view(), name='customer-create'),
    path('customer/<int:id>', views.CustomerDetailView.as_view(), name="customer-detail"),
    path('customer/<int:id>/update/', views.CustomerUpdate.as_view(), name='customer-update'),
]
