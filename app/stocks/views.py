"""Views for the stocks API."""

from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.models import Stock
from stocks import serializers


class StockViewSet(viewsets.ModelViewSet):
    """View for managing stock APIs."""
    serializer_class = serializers.StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [IsAuthenticated]
