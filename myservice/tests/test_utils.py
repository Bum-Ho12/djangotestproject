"""
file: test_utils.py
location:myservice/tests
description: tests the send_sms function in the utils module
"""
import os
from unittest.mock import patch
from dotenv import load_dotenv
from django.test import TestCase
from myservice.utils import send_sms

# Loading env variables
load_dotenv()

class SMSTestCase(TestCase):
    """
    Test case for the send_sms function
    """
    def test_send_bulk_sms(self):
        '''
        Test the send_sms function to send bulk SMS
        '''
        # Mocking the send method of africastalking.SMS
        with patch('africastalking.SMS.send') as mock_send:
            mock_send.return_value = {
                'SMSMessageData': {
                    'Recipients': [
                        {'number': '+1234567890', 'status': 'Success', 'messageId': '123'},
                        {'number': os.environ.get('TEST_NUMBER2'),
                            'status': 'Success', 'messageId': '456'}
                    ]
                }
            }

            # Call the function to send bulk SMS
            message = "Test message"
            recipients = ["+1234567890", "+9876543210"]
            send_sms(message, recipients)

            # Assertions
            mock_send.assert_called_once_with(message, recipients)
