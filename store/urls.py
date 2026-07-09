from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('categoria/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('prodotto/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    path('carrello/', views.cart_detail, name='cart_detail'),
    path('carrello/aggiungi/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('carrello/rimuovi/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]