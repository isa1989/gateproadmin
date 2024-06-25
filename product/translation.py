# models.py or translation.py

from django.db import models
from modeltranslation.translator import TranslationOptions, register
from product.models import Product


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
    )  # Add fields you want to translate
