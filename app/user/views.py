"""
Views for the home page.
"""

from django.shortcuts import (
    render,
    )
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken

from user.serializers import AuthTokenSerializer


def home(request):
    "Home page view."
    return render(request, 'home.html')


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
