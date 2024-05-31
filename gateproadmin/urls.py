from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('gatepro/admin/', admin.site.urls),
    path('', include('home.urls')),
    path('customer/', include('customer.urls')),
    path('device/', include('device.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
