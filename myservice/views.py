"""
file: views.py
location:myservice
description: defines the views for the API
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
from .utils import send_sms

class OrderCreateView(APIView):
    """
    OrderCreateView class creates an order for a customer
    """
    # pylint: disable = no-member
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        post method creates an order for a customer
        """
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            customer = request.user
            order = serializer.save(customer=customer)
            # Send SMS notification after successful order creation
            self.send_sms_notification(customer.phone_number, order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_sms_notification(self, phone_number, order):
        """
        send_sms_notification method sends an SMS notification
        """
        message = f"Your order #{order.id} has been created. Thank you for your business!"
        response = send_sms(phone_number, message)
        if response != 'Success':
            print(f"Failed to send SMS notification: {response}")
