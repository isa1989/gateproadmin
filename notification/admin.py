# admin.py
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Notification


class NotificationAdmin(TranslationAdmin):
    list_display = (
        "title",
        "customer",
        "timestamp",
        "isRead",
    )
    list_filter = (
        "timestamp",
        "isRead",
    )
    search_fields = (
        "title",
        "message",
        "customer__name",
    )


admin.site.register(Notification, NotificationAdmin)
