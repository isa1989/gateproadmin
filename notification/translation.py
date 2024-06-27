from modeltranslation.translator import TranslationOptions, register
from .models import NotifyEvent


@register(NotifyEvent)
class NotifyEventTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "message",
    )  # Add fields you want to translate
