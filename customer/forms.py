from django import forms
from customer.models import Customer


class CreateCustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = "__all__"



class UpdateCustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = "__all__"
