from django.contrib import admin
from .models import Product, ProductImage, Order, WebOrder
from modeltranslation.admin import TranslationAdmin


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [
        ProductImageInline,
    ]


admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(WebOrder)
