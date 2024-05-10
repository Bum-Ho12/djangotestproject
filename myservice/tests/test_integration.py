"""
file: test_integration.py
location:myservice/tests
description: tests the integration between the views, models and utils modules
"""
from unittest.mock import patch
from django.test import Client, TestCase
from django.contrib.auth.models import User
from myservice.models import Order

class TestOrderCreation(TestCase):
    """
    Test the creation of an order
    """

    def setUp(self):
        '''
        Set up the test data
        '''
        self.client = Client()
        user = User.objects.create_user(username='testuser',
                password='password123', email='test@example.com')
        self.client.login(username=user.username, password=user.password)

    @patch('myservice.utils.send_sms')
    def test_create_order_with_auth(self,mock_send_sms):
        '''
        Test creating an order with authentication
        '''
        data = {'customer': 1, 'item': 'Test Item', 'amount': 10.99}
        response = self.client.post('/orders/', data=data, format='json')
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'Order created successfully!')

        # Assert order creation in database
        # pylint: disable=no-member
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.get(pk=1)  # Assuming order ID is 1
        self.assertEqual(order.customer, self.client.user)
        self.assertEqual(order.item, 'Test Item')
        self.assertEqual(order.amount, 10.99)

        # Assert SMS sending was called (mocked in this test)
        mock_send_sms.assert_called_once_with(self.client.user.phone_number, ...)
