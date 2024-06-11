from django.contrib import admin
from .models import Product, ProductImage, Order


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]


admin.site.register(ProductImage)
admin.site.register(Order)
