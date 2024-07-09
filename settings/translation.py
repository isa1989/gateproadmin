from modeltranslation.translator import TranslationOptions, register
from .models import PrivacyPolicy, TermsConditions


@register(PrivacyPolicy)
class PrivacyPolicyTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(TermsConditions)
class TermsConditionsTranslationOptions(TranslationOptions):
    fields = ("content",)
