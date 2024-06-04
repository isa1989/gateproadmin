import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from api.serializers import (
    CustomerRegistrationSerializer,
    CustomerSerializer,
    CustomerLoginSerializer,
    OTPSerializer,
)
from customer.models import Customer, OTP, CustomerToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.auth import (
    generate_or_update_jwt_token,
    verify_jwt_token,
    validate_otp_and_generate_token,
)
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.exceptions import NotFound

from api.permissions import IsCustomerAuthenticated, IsOwnerOrReadOnly


class CustomerPhoneRegistrationView(APIView):
    # queryset = Customer.objects.all()
    permission_classes = [AllowAny]

    def post(self, request):
        phone_number = request.data.get("phone_number")
        if not phone_number:
            raise ValidationError("Phone number is missing.")

        existing_customer = Customer.objects.filter(phone_number=phone_number).exists()
        if existing_customer:
            return Response(
                {"detail": "Customer already registered."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if "phone_step" in request.data:
            otp_instance = OTP.objects.filter(phone_number=phone_number).first()
            if otp_instance:
                otp_serializer = OTPSerializer(otp_instance, data=request.data)
            else:
                otp_serializer = OTPSerializer(data=request.data)

            if otp_serializer.is_valid():
                otp_serializer.save()
                return Response(
                    {"detail": "OTP sent successfully"}, status=status.HTTP_200_OK
                )
            return Response(otp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif "otp_step" in request.data:
            try:
                otp_instance = OTP.objects.get(otp_code=request.data["otp_code"])
            except OTP.DoesNotExist:
                return Response(
                    {"detail": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST
                )

            # Check if OTP is associated with the correct phone number
            if otp_instance.phone_number != request.data.get("phone_number"):
                return Response(
                    {"detail": "OTP does not match the provided phone number"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # If OTP is valid, generate JWT token with a 24-hour expiry time
            token = generate_or_update_jwt_token(phone_number)
            return Response({"token": token}, status=status.HTTP_200_OK)

        elif "register_completed" in request.data:
            token = request.headers.get("Authorization")
            if not token:
                return Response(
                    {"detail": "Token is missing."}, status=status.HTTP_400_BAD_REQUEST
                )

            if not verify_jwt_token(token, phone_number):
                return Response(
                    {"detail": "Invalid or expired token."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            serializer = CustomerRegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                updated_token = generate_or_update_jwt_token(phone_number)
                return Response(
                    {
                        "created": True,
                        "token": updated_token,
                    },
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(
                {"detail": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST
            )


class CustomerPhoneLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone_number = request.data.get("phone_number")
        if not phone_number:
            raise ValidationError("Phone number is missing.")

        if "phone_step" in request.data:
            otp_instance = OTP.objects.filter(phone_number=phone_number).first()
            if otp_instance:
                otp_serializer = OTPSerializer(otp_instance, data=request.data)
            else:
                otp_serializer = OTPSerializer(data=request.data)

            if otp_serializer.is_valid():
                otp_serializer.save()
                return Response(
                    {"detail": "OTP sent successfully"}, status=status.HTTP_200_OK
                )
            return Response(otp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif "otp_step" in request.data:
            otp_code = request.data.get("otp_code")
            if not otp_code:
                return Response(
                    {"detail": "OTP code is missing."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            try:
                otp_instance = OTP.objects.get(otp_code=otp_code)
            except OTP.DoesNotExist:
                return Response(
                    {"detail": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST
                )

            if otp_instance.phone_number != phone_number:
                return Response(
                    {"detail": "OTP does not match the provided phone number"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            token = generate_or_update_jwt_token(phone_number)
            return Response({"token": token}, status=status.HTTP_200_OK)

        else:
            return Response(
                {"detail": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST
            )


class CustomerLogoutView(APIView):
    queryset = Customer.objects.all()
    permission_classes = [IsCustomerAuthenticated]

    def post(self, request):
        token = request.headers.get("Authorization")
        phone_number = request.data.get("phone_number")
        if not token:
            return Response(
                {"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not phone_number:
            return Response(
                {"error": "Phone number is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            customer_token = CustomerToken.objects.get(
                token=token, phone_number=phone_number
            )
            customer_token.delete()
            return Response(
                {"message": "User logged out successfully"}, status=status.HTTP_200_OK
            )
        except CustomerToken.DoesNotExist:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
            )


class CustomerDeleteView(APIView):
    permission_classes = [IsCustomerAuthenticated, IsOwnerOrReadOnly]

    def delete(self, request, *args, **kwargs):
        token = request.headers.get("Authorization")
        customer_id = request.data.get("customer_id")

        if not token:

            return Response(
                {"error": "Token is required"}, status=status.HTTP_401_UNAUTHORIZED
            )

        customer_token = get_object_or_404(CustomerToken, token=token)
        customer = customer_token.customer
        if not customer:
            return Response(
                {"error": "Customer does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        if customer_id and str(customer.id) != customer_id:
            return Response(
                {"error": "Invalid customer ID"}, status=status.HTTP_400_BAD_REQUEST
            )
        if customer != Customer.objects.get(id=customer_id):
            return Response(
                {"error": "You are not authorized to delete this profile"},
                status=status.HTTP_403_FORBIDDEN,
            )
        customer.delete()
        return Response(
            {"message": "Customer profile deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class CustomerProfileEditView(RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
