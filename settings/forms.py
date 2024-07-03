# forms.py

from django import forms
from .models import PlayStoreFormSubmission


class PlayStoreForm(forms.ModelForm):
    class Meta:
        model = PlayStoreFormSubmission
        fields = ["number", "email", "reason", "other_reason"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["reason"].widget.attrs.update({"class": "reason-select"})

    def clean(self):
        cleaned_data = super().clean()
        reason = cleaned_data.get("reason")
        other_reason = cleaned_data.get("other_reason")

        if reason == "other" and not other_reason:
            raise forms.ValidationError("Please specify the reason.")

        return cleaned_data
