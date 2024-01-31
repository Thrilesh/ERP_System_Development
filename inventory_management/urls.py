from django.urls import path
from .views import create_product, product_list, create_stock_movement, stock_movement_list, create_inventory, inventory_list

urlpatterns = [
    path('product/create/', create_product, name='create_product'),
    path('product/list/', product_list, name='product_list'),
    path('stock-movement/create/', create_stock_movement,
         name='create_stock_movement'),
    path('stock-movement/list/', stock_movement_list, name='stock_movement_list'),
    path('inventory/create/', create_inventory, name='create_inventory'),
    path('inventory/list/', inventory_list, name='inventory_list'),
]
