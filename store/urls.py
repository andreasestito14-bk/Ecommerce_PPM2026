from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('categoria/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('prodotto/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]