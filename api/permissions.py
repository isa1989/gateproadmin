from rest_framework.permissions import BasePermission
from customer.models import CustomerToken


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


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to allow only the owner of an object to delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow DELETE requests only if the authenticated user is the owner of the object
        return obj == request.user
