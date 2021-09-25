from django.contrib import admin
from django.contrib.admin.decorators import display
from django.db import models

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'city', 'created', 'updated', 'paid']
    inlines = [OrderItemInline]
