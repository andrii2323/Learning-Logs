from django.urls import path
from . import views

app_name = 'reminders'

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('new/', views.new_reminder, name='new_reminder'),
    path('delete/<int:pk>/', views.delete_reminder, name='delete_reminder'),
]