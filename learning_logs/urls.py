'''Defines URL patters for learning_logs'''

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Main page
    path('', views.index, name='index'),
    # A page displaying topics
    path('topics/', views.topics, name='topics'),
    # A page devoted to a separate topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # A page for add a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # A page to add a new post
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # A page for editing post
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]