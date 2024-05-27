from django.urls import path
from . import views

urlpatterns = [
    path('devices/', views.DeviceListView.as_view(), name="device-list"),
    path('add-device/', views.DeviceCreateView.as_view(), name="add-device"),
]