"""Defines schemas URL for learning_logs."""

from django.urls import path
from .views import *


app_name = 'learning_logs'
urlpatterns = [
    path('', index, name='index'),
    path('topics/', topics, name='topics'),
    path('topics/<int:id>/', read_topic, name='topic'),
    path('new_topic/', TopicCreate.as_view(), name='new_topic'),
    path('new_entry/<int:topic_id>/', EntryCreate.as_view(), name='new_entry'),
    path('entry/<int:entry_id>/edit/', edit_entry, name='edit_entry'),
    path('entry/<int:id>/', EntryDetail.as_view(), name='entry'),
]
