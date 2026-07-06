from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Product, Category


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-created_at')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'store/product_list.html', context)


class ProductDetailView(DetailView):
    # Requisito obbligatorio: Class-Based View
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'