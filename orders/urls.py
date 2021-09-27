from django.urls import path

from orders.views import order_create

urlpatterns = [
    path('create/', order_create, name='create')
]