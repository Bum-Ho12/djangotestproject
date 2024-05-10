'''
file: models.py
location:myservice
description: defines the models for the API
'''

from django.db import models


class Customer(models.Model):
    '''
    Customer model class contains Customer DB field for the REST API
    '''
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    '''
    Order model class contains Order DB fields for the REST API
    '''
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} - {self.amount}"
