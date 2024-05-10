"""
file: admin.py
location:myservices
description: defines the admin for the API
"""
from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Customer)
admin.site.register(models.Order)
