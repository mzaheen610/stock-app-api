"""
URLS for the stocks API
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stocks import views


router = DefaultRouter()
router.register('stocks', views.StockViewSet)

app_name = 'stocks'

urlpatterns = [
    path('', include(router.urls)),
]
