"""
Serializers for the user api view.
"""

from django.contrib.auth import (
    get_user_model,
    authenticate,
    )
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

# class UserSerializer(serializers.ModelSerializer):
#     """Serializer for the user model"""

#     class Meta:
#         model = get_user_model()
#         fields = ['email', 'password']
#         extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token"""

    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _("Unable to authenticate user with provided credentials.")
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
