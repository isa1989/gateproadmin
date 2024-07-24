from django.db import models
from customer.models import Customer


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    thumbnail = models.ImageField(
        upload_to="thumbnails/"
    )  # Thumbnail image for the product

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="product_images/"
    )  # Additional images for the product

    def __str__(self):
        return f"Image for {self.product.name}"

    class Meta:
        ordering = ["id"]


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Shipped", "Shipped"),
    ]

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE
    )  # Assuming you have a Customer model
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES)

    def __str__(self):
        return f"Order {self.id} - {self.customer}"

    class Meta:
        ordering = ["id"]


class WebOrder(models.Model):
    ORDER_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Shipped", "Shipped"),
    ]
    phone_number = models.CharField(max_length=13)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES)

    def __str__(self):
        return self.phone_number

    class Meta:
        ordering = ["id"]
