from cart.cart import Cart
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import OrderCreateForm
from .models import OrderItem


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])

            cart.clear()
            messages.success(request, 'Your order has been successfully completed.')
            return HttpResponseRedirect('/')

    else:
        form = OrderCreateForm()

    context = {'form': form, 'cart': cart}
    return render(request, 'orders/created.html', context)
