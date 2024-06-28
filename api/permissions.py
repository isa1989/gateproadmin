from rest_framework.permissions import BasePermission
from customer.models import CustomerToken
from api.auth.auth import get_customer_from_token


class IsCustomerAuthenticated(BasePermission):
    """
    Custom permission to check if a customer is authenticated.
    """

    def has_permission(self, request, view):
        # Retrieve the token from the request headers
        token = request.headers.get("Authorization")
        if not token:
            return False

        # Extract the token from the Authorization header
        token = token.split()[1] if token.startswith("Bearer ") else token

        try:
            # Check if the CustomerToken exists
            customer_token = CustomerToken.objects.get(token=token)
            return True
        except CustomerToken.DoesNotExist:
            return False


class IsOwnerOfDevice(BasePermission):
    def has_object_permission(self, request, view, obj):
        token = request.headers.get("Authorization")
        customer = get_customer_from_token(token)
        return obj.owner == customer
