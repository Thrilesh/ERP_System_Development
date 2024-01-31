from django import forms
from .models import Product, StockMovement, Inventory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'sku']


class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
        fields = ['description']


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity']
