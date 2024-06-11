from rest_framework import serializers
from product.models import Product, Order
from api.auth.auth import get_customer_from_token


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    has_order = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "discount_price",
            "thumbnail",
            "images",
            "has_order",
        ]

    def get_images(self, obj):
        return [image.image.url for image in obj.images.all()]

    def get_has_order(self, obj):
        customer = get_customer_from_token(
            self.context["request"].headers.get("Authorization")
        )
        return Order.objects.filter(
            product=obj.id, customer=customer, status="Pending"
        ).exists()
