from django import forms
from device.models import Device


class CreateDeviceForm(forms.ModelForm):
    
    class Meta:
        model = Device
        fields = "__all__"


