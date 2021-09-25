from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=240, verbose_name='First name', blank=False)
    last_name = models.CharField(max_length=240, verbose_name='Last name', blank=False)
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=14, verbose_name='Phone', blank=False)
    address = models.CharField(max_length=240, verbose_name='Address', blank=False)
    city = models.CharField(max_length=240, verbose_name='City')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
