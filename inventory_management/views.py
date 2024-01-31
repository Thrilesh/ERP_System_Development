from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, StockMovement, Inventory
from .forms import ProductForm, StockMovementForm, InventoryForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory_management/product_list.html', {'products': products})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory_management/product_form.html', {'form': form})


def stock_movement_list(request):
    movements = StockMovement.objects.all()
    return render(request, 'inventory_management/stock_movement_list.html', {'movements': movements})


def create_stock_movement(request):
    if request.method == 'POST':
        form = StockMovementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_movement_list')
    else:
        form = StockMovementForm()
    return render(request, 'inventory_management/stock_movement_form.html', {'form': form})


def inventory_list(request):
    inventories = Inventory.objects.all()
    return render(request, 'inventory_management/inventory_list.html', {'inventories': inventories})


def create_inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    return render(request, 'inventory_management/inventory_form.html', {'form': form})
