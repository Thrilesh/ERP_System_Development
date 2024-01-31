# purchase_management/urls.py

from django.urls import path
from .views import create_supplier, update_supplier, delete_supplier, supplier_list

urlpatterns = [
    path('supplier/create/', create_supplier, name='create_supplier'),
    path('supplier/list/', supplier_list, name='supplier_list'),
    path('supplier/<int:pk>/update/', update_supplier, name='update_supplier'),
    path('supplier/<int:pk>/delete/', delete_supplier, name='delete_supplier'),
]
