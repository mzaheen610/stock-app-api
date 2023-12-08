"""
Serializers for the stocks API.
"""

from rest_framework import serializers
from core.models import Stock


class StockSerializer(serializers.ModelSerializer):
    """Serializer for the stock API."""

    class Meta:
        model = Stock
        fields = ['name', 'price']
