from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

urlpatterns = [
    path("gatepro/admin/", admin.site.urls),  # Admin URL
    path("", include("home.urls")),  # Main application URL
    path("customer/", include("customer.urls")),
    # path("device/", include("device.urls")),
    path("api/", include("api.urls")),  # API URL
    path("api-auth/", include("rest_framework.urls")),  # Django Rest Framework auth URL
    path("settings/", include("settings.urls")),
]

# Serving media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serving static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Internationalization patterns for i18n URLs
urlpatterns += i18n_patterns(
    path("api/", include("api.urls")),  # Adjust to your app's specific URLs
    # Add other internationalized paths as needed
)
