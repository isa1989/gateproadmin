import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerRegistrationSerializer
from customer.models import Customer, OTP, CustomerToken
from rest_framework.permissions import AllowAny
from datetime import datetime, timedelta, timezone
from django.conf import settings




# def generate_jwt_token(customer_instance):
#     token_payload = {
#         'customer_id': customer_instance.id,
#         'exp': datetime.now(timezone.utc) + timedelta(hours=24)  # Token expiration time
#     }
#     token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm='HS256')
#     token_instance = CustomerToken.objects.create(customer=customer_instance.id, token=token)
#     return token

def generate_or_update_jwt_token(customer_instance):
    # Create the token payload without an expiration date
    
    token_payload = {
        'customer_id': customer_instance.id,
        'timestamp': datetime.now(timezone.utc).timestamp()
    }
    token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm='HS256')
    # Save or update the token instance
    token_instance, _ = CustomerToken.objects.update_or_create(customer=customer_instance, defaults={'token': token})
    return token

def verify_jwt_token(token, customer_id):
    try:
        # Check if the token exists in the database
        token_obj = CustomerToken.objects.get(token=token, customer=customer_id)
        # Token exists and is valid
        return True
    except CustomerToken.DoesNotExist:
        # Token does not exist in the database
        return False

class CustomerPhoneRegistrationView(APIView):
    queryset = Customer.objects.all()
    permission_classes = [AllowAny] 
    def post(self, request):
        serializer = CustomerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            customer_instance = serializer.save()
            otp = OTP.objects.create(customer=customer_instance)
            return Response({"customer_id": customer_instance.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        data = request.data
        token = request.headers.get('Authorization')
        customer_id = data.get("customer_id")
        
        if data.get("register_completed"):
            if verify_jwt_token(token, customer_id):
                try:
                    # Retrieve customer information and store it in a variable
                    customer_instance = Customer.objects.get(id=customer_id)
                except Customer.DoesNotExist:
                    return Response({"message": "Customer does not exist."}, status=status.HTTP_400_BAD_REQUEST)

                serializer = CustomerRegistrationSerializer(customer_instance, data=request.data, partial=True)
                if serializer.is_valid():
                    token = generate_or_update_jwt_token(customer_instance)
                    serializer.save()
                    return Response({**serializer.data, "token": token}, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

        try:
            otp_instance = OTP.objects.get(otp_code=data.get('otp_code'))
        except OTP.DoesNotExist:
            otp_instance = None
            
        if otp_instance:
            customer_instance = otp_instance.customer
            if customer_instance.id != customer_id:
                return Response({"message": "Invalid OTP code."}, status=status.HTTP_400_BAD_REQUEST)
            
            token = generate_or_update_jwt_token(customer_instance)
            response_data = {
                "customer_id": customer_instance.id,
                "token": token
            }
            return Response(response_data, status=status.HTTP_200_OK)
        
        return Response({"message": "Invalid OTP code."}, status=status.HTTP_400_BAD_REQUEST)


