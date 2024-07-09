from django.contrib import admin
from .models import Settings, PlayStoreFormSubmission, PrivacyPolicy, TermsConditions
from modeltranslation.admin import TranslationAdmin


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(TranslationAdmin):
    pass


@admin.register(TermsConditions)
class TermsConditionsAdmin(TranslationAdmin):
    pass


admin.site.register(Settings)
admin.site.register(PlayStoreFormSubmission)
