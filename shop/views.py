from django.shortcuts import render

from cart.forms import CartAddProductForm
from shop.models import Product, Advertisement


def home(requests):
    product_sort = Product.objects.all()[:4]
    products = Product.objects.all()
    advertisement = Advertisement.objects.all()[:3]
    advertisement_last = Advertisement.objects.last()
    cart_product_form = CartAddProductForm()
    context = {
        'product_sort': product_sort,
        'products': products,
        'advertisement': advertisement,
        'advertisement_last': advertisement_last,
        'cart_product_form': cart_product_form
    }

    return render(requests, 'main/home.html', context)
