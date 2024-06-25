# admin.py
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import FAQ


class FAQAdmin(TranslationAdmin):
    list_display = ("question",)
    search_fields = (
        "question",
        "answer",
    )


admin.site.register(FAQ, FAQAdmin)
