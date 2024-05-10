"""
file: oidc_config.py
location:myservice
description: defines the OIDC configuration for the API
"""
import os
from oauth2_provider.settings import oauth2_settings
from dotenv import load_dotenv

# Loading env variables
load_dotenv()

OIDC_SETTINGS = {
    'CLIENT_ID': os.environ.get('AUTH_CLIENT_ID'),
    'CLIENT_SECRET': os.environ.get('AUTH_CLIENT_SECRET'),
    'SCOPES': ['openid', 'profile', 'email'],
    'DISCOVERY_URL': 'https://accounts.google.com/.well-known/openid-configuration',
    'OAUTH2_PROVIDER_CALLBACK': 'http://localhost:8000/callback',
    'OIDC_ENDPOINT_AUTO_DISCOVERY': True,
    'BEARER_TOKEN_BACKEND': 'oauth2_provider.backends.OAuth2TokenBackend',
    'REQUIRED_SCOPES': ['openid', 'profile'],
}

oauth2_settings.update(OIDC_SETTINGS)
