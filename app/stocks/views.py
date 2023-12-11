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


class StockViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """View for managing stock APIs."""
    serializer_class = serializers.StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        """Filter the queryset for listing only available stocks."""
        queryset = self.queryset
        queryset = queryset.filter(user__isnull=True)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        """Purchase stock by a user."""
        user = request.user
        instance = self.get_object()
        stock = Stock.objects.get(name=instance.name)
        stock.user = user
        stock.save()
        
        serializer = self.get_serializer(stock)

        # return Response(serializer.data)
        return Response(f'Stock {stock.name} has been purchased by user {user.email}')
