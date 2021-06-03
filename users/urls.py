"""Defines schemas URL for users."""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # log in
    path('', include('django.contrib.auth.urls')),
    # register new user
    path('register/', views.register, name='register'),
]
