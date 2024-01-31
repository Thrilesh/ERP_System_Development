from django.shortcuts import get_object_or_404, redirect, render

from .forms import SupplierForm
from .models import Supplier

# Create your views here.


def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'purchase_management/supplier_list.html', {'suppliers': suppliers})


def create_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'purchase_management/supplier_form.html', {'form': form})


def update_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'purchase_management/supplier_form.html', {'form': form})


def delete_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    return redirect('supplier_list')
