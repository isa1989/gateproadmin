from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SettingsViewSet

router = DefaultRouter()
router.register(r'settings', SettingsViewSet, basename='settings')

urlpatterns = [
    path('', include(router.urls)),
    path('settings/banner_image/', SettingsViewSet.as_view({'get': 'banner_image'})),
]
