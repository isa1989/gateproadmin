from django.contrib import admin
from .models import Settings, PlayStoreFormSubmission, PrivacyPolicy, TermsConditions

admin.site.register(Settings)
admin.site.register(PlayStoreFormSubmission)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsConditions)
