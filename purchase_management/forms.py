# purchase_management/forms.py
from django import forms
from .models import Supplier, PurchaseOrder


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['first_name', 'last_name', 'email', 'phone']


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['supplier', 'order_status', 'purchase_notes']
