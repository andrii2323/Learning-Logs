from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # Auth
    path('', include('django.contrib.auth.urls')),
    # Registration
    path('register/', views.register, name='register'),
]