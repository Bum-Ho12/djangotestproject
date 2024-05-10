"""
file: views.py
location:myservice
description: defines the views for the API
"""
import os
import africastalking
from dotenv import load_dotenv

# Loading env variables
load_dotenv()

# Africa's Talking credentials (sandbox)
USERNAME = 'sandbox'
api_key = os.environ.get('AT_KEY')
africastalking.initialize(USERNAME, api_key)

CLIENT = africastalking.SMS

def send_sms(phone_number, message):
    '''
    send_sms function sends an SMS to a phone number
    using the Africa's Talking API.
    '''
    try:
        # Using sandbox environment for testing
        response = CLIENT.send(message, [phone_number])
        return response['recipients'][0]['status']
    # pylint: disable=broad-except
    except Exception as e:
        print(e)
        return str(e)
