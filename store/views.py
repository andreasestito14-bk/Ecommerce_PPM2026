from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from .models import Product, Category, Order, OrderItem
from django.contrib.auth.decorators import login_required


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
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'


@login_required(login_url='accounts:login')
def cart_detail(request):
    order, created = Order.objects.get_or_create(user=request.user, status='pending')
    context = {'order': order}
    return render(request, 'store/cart_detail.html', context)


@login_required(login_url='accounts:login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, status='pending')

    order_item, item_created = OrderItem.objects.get_or_create(order=order, product=product, defaults={'price': product.price, 'quantity': 1})

    if not item_created:
        order_item.quantity += 1
        order_item.save()

    return redirect('store:cart_detail')


@login_required(login_url='accounts:login')
def remove_from_cart(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id, order__user=request.user)
    item.delete()
    return redirect('store:cart_detail')