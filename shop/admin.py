from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Advertisement


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'image_product', 'price', 'created_at', 'available')
    list_display_links = ('id', 'title', 'slug', 'category')
    search_fields = ('title', 'category')
    prepopulated_fields = {"slug": ("title",)}

    # Show image in django admin panel
    def image_product(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_product.__name__ = "Image"


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image_advertisement', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    # Show image in django admin panel
    def image_advertisement(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_advertisement.__name__ = "Image"