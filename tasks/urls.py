from django.contrib import admin
from django.urls import path, include
from . import views as chat_views

urlpatterns = [
    path('tasks/', chat_views.tasks_home, name='Tasks-home'),
    
]