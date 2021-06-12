"""Defines schemas URL for learning_logs."""

from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'learning_logs'
urlpatterns = [
    # homepage
    path('', views.index, name='index'),
    # page with all topics
    path('topics/', views.topics, name='topics'),
    # topic all entries
    path('topics/<int:id>/', login_required(views.TopicDetail.as_view()), name='topic'),
    # create new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # create new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # edit entry
    path('entry/<int:entry_id>/edit/', views.edit_entry, name='edit_entry'),
    # read entry
    path('entry/<int:id>/', login_required(views.EntryDetail.as_view()), name='entry'),
]
