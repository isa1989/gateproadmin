import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from api.auth.serializers import (
    CustomerSerializer,
    OTPSerializer,
)
from customer.models import Customer, OTP, CustomerToken
from rest_framework.permissions import AllowAny
from api.auth.auth import (
    generate_or_update_jwt_token,
    get_phone_number_from_token,
    get_customer_from_token,
)
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.exceptions import NotFound
from notification.notification import send_sms
from api.permissions import IsCustomerAuthenticated


class CustomerPhoneRegistrationView(APIView):
    # queryset = Customer.objects.all()
    permission_classes = [IsCustomerAuthenticated]

    def post(self, request):
        token = request.headers.get("Authorization")
        if not token:
            return Response(
                {"error": "Token is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        name = request.data.get("name")
        surname = request.data.get("surname")
        phone_number = get_phone_number_from_token(token)

        if not name and not surname:
            error_message = "Both name and surname are required."
        elif not name:
            error_message = "Name is required."
        elif not surname:
            error_message = "Surname is required."

            return Response(
                {"detail": error_message},
                status=status.HTTP_400_BAD_REQUEST,
            )
        customer_data = {
            "name": name,
            "surname": surname,
            "phone_number": phone_number,
            "is_active": True,
        }
        try:
            # Try to retrieve the customer based on phone number
            customer = Customer.objects.get(phone_number=phone_number, is_active=False)
            serializer = CustomerSerializer(customer, data=customer_data, partial=True)

        except Customer.DoesNotExist:
            serializer = CustomerSerializer(data=customer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"data": serializer.data, "message": "User profile updated"},
            status=status.HTTP_200_OK,
        )


class CustomerPhoneLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request, "postttttttttttttttttttttttttttttttttttttttttttt")
        phone_number = request.data.get("phone_number")
        if not phone_number:
            raise ValidationError("Phone number is missing.")

        otp_instance = OTP.objects.filter(phone_number=phone_number).first()
        if otp_instance:
            otp_serializer = OTPSerializer(otp_instance, data=request.data)
        else:
            otp_serializer = OTPSerializer(data=request.data)

        if otp_serializer.is_valid():
            otp = otp_serializer.save()
            # sms = send_sms(phone_number, otp.otp_code)
            temporary_token = generate_or_update_jwt_token(phone_number)
            response_data = {
                "data": {"token": temporary_token},
                "message": "Temporary token generated",
            }

            return Response(response_data, status=status.HTTP_200_OK)
        return Response(otp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerPhoneVerifyOtpView(APIView):
    permission_classes = [IsCustomerAuthenticated]

    def post(self, request):
        token = request.headers.get("Authorization")
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
        phone_number = get_phone_number_from_token(token)
        if otp_instance.phone_number != phone_number:
            return Response(
                {"detail": "OTP does not match the provided phone number"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        primary_token = generate_or_update_jwt_token(phone_number)
        is_registered = Customer.objects.filter(
            phone_number=phone_number, is_active=True
        ).exists()
        if is_registered:
            message = "User verified and authenticated"
        else:
            message = "User verified, registration required"
        response_data = {
            "data": {"token": primary_token, "registered": is_registered},
            "message": message,
        }
        return Response(response_data, status=status.HTTP_200_OK)


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
    permission_classes = [IsCustomerAuthenticated]

    def delete(self, request, *args, **kwargs):
        token = request.headers.get("Authorization")
        customer = get_customer_from_token(token)

        if not token:
            return Response(
                {"error": "Token is required"}, status=status.HTTP_401_UNAUTHORIZED
            )
        customer.is_active = False
        customer.save()

        return Response(
            {"message": f"Customer  has been deleted."},
            status=status.HTTP_204_NO_CONTENT,
        )


def transform_request_data(customer, request_data):
    transformed_data = {
        "firebase_token": request_data.get("firebaseToken", customer.firebase_token),
        "language": request_data.get("language"),
        "email": request_data.get("notificationPreferences", {}).get(
            "email", customer.email
        ),
        "sms": request_data.get("notificationPreferences", {}).get("sms", customer.sms),
        "push": request_data.get("notificationPreferences", {}).get(
            "push", customer.push
        ),
        "name": request_data.get("name", customer.name),
        "surname": request_data.get("surname", customer.surname),
    }
    return transformed_data


class ProfileUpdateAPIView(APIView):
    permission_classes = [IsCustomerAuthenticated]

    def get(self, request, *args, **kwargs):
        token = request.headers.get("Authorization")
        customer = get_customer_from_token(token)
        data = {
            "userId": customer.pk,
            "firebaseToken": customer.firebase_token,
            "language": "en",
            "notificationPreferences": {
                "email": customer.email,
                "sms": customer.sms,
                "push": customer.push,
            },
            "name": customer.name,
            "surname": customer.surname,
        }
        return Response(data)

    def patch(self, request, *args, **kwargs):
        token = request.headers.get("Authorization")
        customer = get_customer_from_token(token)
        transformed_data = transform_request_data(customer, request.data)
        serializer = CustomerSerializer(customer, data=transformed_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User profile updated successfully."})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
