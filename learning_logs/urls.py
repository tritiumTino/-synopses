"""Defines schemas URL for learning_logs."""

from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # homepage
    path('', views.index, name='index'),
    # page with all topics
    path('topics/', views.topics, name='topics'),
    # topic all entries
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # create new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # create new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
