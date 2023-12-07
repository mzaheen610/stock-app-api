"""
Views for the home page.
"""

from django.shortcuts import render, redirect


def home(request):
    "Home page view."
    return render(request, 'home.html')