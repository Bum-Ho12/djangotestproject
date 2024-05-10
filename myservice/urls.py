'''
file: urls.py
location:myservice
description: defines the URL patterns for the API
'''

from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderCreateView.as_view(), name='order-create'),
]
