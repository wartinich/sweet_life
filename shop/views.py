from django.shortcuts import render

from shop.models import Product, Advertisement


def home(requests):
    product_sort = Product.objects.all()[:4]
    products = Product.objects.all()
    advertisement = Advertisement.objects.all()[:3]
    advertisement_last = Advertisement.objects.last()
    context = {
        'product_sort': product_sort,
        'products': products,
        'advertisement': advertisement,
        'advertisement_last': advertisement_last
    }

    return render(requests, 'main/base.html', context)
