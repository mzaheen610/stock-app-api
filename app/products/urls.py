"""
URL mappings for the products page.
"""

from django.urls import path
from products import views

urlpatterns = [
    path('products', views.products_view, name='products'),
]