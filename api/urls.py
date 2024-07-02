# api/urls.py
from django.urls import path
from api.auth.views import (
    CustomerPhoneRegistrationView,
    ProfileUpdateAPIView,
    CustomerPhoneLoginView,
    CustomerLogoutView,
    CustomerDeleteView,
    CustomerPhoneVerifyOtpView,
)
from api.product.views import (
    ProductListView,
    ProductDetailView,
    CreateOrUpdateProductOrder,
)
from api.faq.views import FAQListView, FAQDetailView, MarkFAQHelpful, MarkFAQNotHelpful
from api.notification.views import (
    NotificationListView,
    NotificationDetailView,
    UnreadNotificationCountView,
    MarkAllNotificationsAsReadView,
)
from api.device.views import (
    DeviceListView,
    DeviceDetailView,
    DevicePinDetailAPIView,
    InviteMemberAPIView,
    RemoveMemberFromDeviceAPIView,
    DeviceMembersListView,
    CarPlateCreateAPIView,
    CarPlateDetailAPIView,
)

urlpatterns = [
    # ------------------------Auth--------------------------
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
    path("customer/delete/", CustomerDeleteView.as_view(), name="customer_delete"),
    # ----------------Endpoint for products---------------------
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path(
        "products/orders/",
        CreateOrUpdateProductOrder.as_view(),
        name="create_or_update_product_order",
    ),
    # ---------------------Endpoint for FAQ-----------------------
    path("faqs/", FAQListView.as_view(), name="faqs_list"),
    path("faqs/<int:id>/", FAQDetailView.as_view(), name="faq_detail"),
    path(
        "faqs/<int:id>/helpful/",
        MarkFAQHelpful.as_view(),
        name="mark_faq_as_helpful",
    ),
    path(
        "faqs/<int:id>/not-helpful/",
        MarkFAQNotHelpful.as_view(),
        name="mark_faq_as_helpful",
    ),
    # -----------------------Notification--------------------------
    path("notifications/", NotificationListView.as_view(), name="notifications-list"),
    path(
        "notifications/count/",
        UnreadNotificationCountView.as_view(),
        name="unread-count",
    ),
    path(
        "notifications/read-all/",
        MarkAllNotificationsAsReadView.as_view(),
        name="mark_all_notifications_as_read",
    ),
    path(
        "notifications/<str:pk>/",
        NotificationDetailView.as_view(),
        name="notification-detail",
    ),
    # -----------------------User Profile API--------------------------
    path("profile/", ProfileUpdateAPIView.as_view(), name="profile-update"),
    # -----------------------Device API--------------------------
    path("devices/", DeviceListView.as_view(), name="devices-list"),
    path("devices/<int:pk>/", DeviceDetailView.as_view(), name="device-detail-unlink"),
    path(
        "devices/<int:device_id>/pins/<int:pin_id>/",
        DevicePinDetailAPIView.as_view(),
        name="device-pin-update",
    ),
    path(
        "devices/<int:deviceId>/invite/",
        InviteMemberAPIView.as_view(),
        name="device-invite",
    ),
    path(
        "devices/<int:deviceId>/members/<int:memberId>/",
        RemoveMemberFromDeviceAPIView.as_view(),
        name="remove-member-from-device",
    ),
    path(
        "devices/<int:deviceId>/members/",
        DeviceMembersListView.as_view(),
        name="device-member-list",
    ),
    # -----------------------Car Plate API--------------------------
    path("car-plates/", CarPlateCreateAPIView.as_view(), name="car_plate_create"),
    path(
        "car-plates/<int:pk>/", CarPlateDetailAPIView.as_view(), name="car-plate-detail"
    ),
]
