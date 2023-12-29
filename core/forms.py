# core/forms.py
from django import forms
from .models import Invoice

class InvoiceAdminForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
