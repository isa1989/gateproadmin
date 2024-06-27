# admin.py
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Notification, NotifyEvent


class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "timestamp",
        "isRead",
    )
    list_filter = (
        "timestamp",
        "isRead",
    )
    search_fields = ("customer__name",)


admin.site.register(Notification, NotificationAdmin)


class NotifyEventAdmin(TranslationAdmin):
    list_display = (
        "title",
        "message",
        "timestamp",
    )
    list_filter = (
        "title",
        "timestamp",
    )
    search_fields = ("title",)


admin.site.register(NotifyEvent, NotifyEventAdmin)
