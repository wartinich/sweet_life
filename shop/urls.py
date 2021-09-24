from django.urls import path

from shop.views import home

urlpatterns = [
    path('', home, name='home')
]
