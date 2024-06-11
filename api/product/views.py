from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from api.permissions import IsCustomerAuthenticated
from product.models import Product, Order
from .serializers import ProductSerializer
from rest_framework import status
from api.auth.auth import get_customer_from_token


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsCustomerAuthenticated]


class ProductDetailView(RetrieveAPIView):
    # permission_classes = [IsCustomerAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class CreateOrUpdateProductOrder(CreateAPIView):
    permission_classes = [IsCustomerAuthenticated]
    queryset = Order.objects.none()

    def post(self, request, *args, **kwargs):
        token = request.headers.get("Authorization")
        data = request.data
        product_id = data.get("productId")
        customer = get_customer_from_token(token)

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the order already exists for the product and customer
        order, created = Order.objects.get_or_create(
            customer=customer, product=product, status="Pending"
        )
        response_data = {"orderId": order.id, "status": order.status}
        status_code = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response(
            response_data,
            status=status_code,
        )
