# api/urls.py
from django.urls import path
from api.auth.views import (
    CustomerPhoneRegistrationView,
    CustomerProfileEditView,
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
    # Endpoint for products
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path(
        "products/orders/",
        CreateOrUpdateProductOrder.as_view(),
        name="create_or_update_product_order",
    ),
    # Endpoint for FAQ
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
]
