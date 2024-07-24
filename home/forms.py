from django import forms
from product.models import WebOrder


class WebOrderForm(forms.ModelForm):
    class Meta:
        model = WebOrder
        fields = ["phone_number", "product", "status"]

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number", "")

        # Remove prefix +994 for validation
        # if phone_number.startswith("+994"):
        #     phone_number = phone_number[4:]

        # Check if phone number is 9 digits long
        if len(phone_number[4:]) != 9 or not phone_number[4:].isdigit():
            raise forms.ValidationError("Phone number must be exactly 9 digits long.")

        # Check if phone number starts with forbidden digits
        if phone_number[4:][0] in "01234":
            raise forms.ValidationError(
                "Phone number cannot start with 0, 1, 2, 3, or 4."
            )

        return phone_number
