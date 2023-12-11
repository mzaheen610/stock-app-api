"""
Views for the products page.
"""
from django.shortcuts import render


def products_view(request):
    """View for the /products endpoint."""
    return render(request, 'products.html')
