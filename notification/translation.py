# models.py or translation.py

from django.db import models
from modeltranslation.translator import TranslationOptions, register
from .models import Notification


@register(Notification)
class NotificationTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "message",
    )  # Add fields you want to translate
