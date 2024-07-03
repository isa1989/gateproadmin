from django.urls import path
from . import views

urlpatterns = [
    path("playstore/form/", views.playstore_form, name="playstore_form"),
    path("form-submitted/", views.form_submitted, name="form_submitted"),
    path("privacy-policy/", views.privacy_policy_view, name="privacy_policy"),
    path("terms-conditions/", views.terms_conditions_view, name="terms_conditions"),
]
