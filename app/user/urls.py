"""
Url patterns for the home page
"""

from django.urls import path
from user import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('token/', views.CreateTokenView.as_view(), name = 'token'),
]