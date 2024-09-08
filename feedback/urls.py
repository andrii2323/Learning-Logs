from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    path('new_feedback/', views.new_feedback, name='new_feedback'),
    path('thanks/', views.feedback_thanks, name='feedback_thanks'),
]