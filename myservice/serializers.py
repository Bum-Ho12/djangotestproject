"""
file: serializers.py
location:myservice
description: defines the serializers for the API
"""

from rest_framework import serializers
from .models import Order, Customer

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer model"""
    class Meta:
        '''
        Meta class for CustomerSerializer
        '''
        model = Customer
        fields = ['id', 'name', 'email', 'phone_number']

class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model"""

    class Meta:
        '''
        Meta class for OrderSerializer
        '''
        model = Order
        fields = '__all__'
