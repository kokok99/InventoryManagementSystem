
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('per_product/<int:pk>', views.per_product_views, name='per_product'),
    path('add_inventory/', views.add_product, name='add_inventory'),
    path('delete/<int:pk>', views.delete_inventory, name='delete_inventory'),
    path('update/<int:pk>', views.update_inventory, name='update_inventory'),
    path('dashboard/', views.dashboard, name='dashboard')
]

