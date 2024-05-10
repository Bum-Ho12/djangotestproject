"""
file: test_models
location:myservice/tests
description: tests the Order model
"""

from django.test import TestCase
from myservice.models import Customer, Order

class TestOrderModel(TestCase):
    """
    Test the Order model
    """

    def test_create_order(self):
        '''
        Test creating an order
        '''
        # pylint: disable = no-member
        customer = Customer.objects.create(name='John Doe',
                        email='john.doe@example.com',phone_number='+254712345678')
        order = Order.objects.create(customer=customer, item='Test Item', amount=10.99)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.item, 'Test Item')
        self.assertEqual(order.amount, 10.99)
