from django.contrib import admin
from django.urls import path, include
from . import views as chat_views

urlpatterns = [
    path('tasks/', chat_views.tasks_home, name='Tasks-home'),
    path('delete_task/<int:task_id>/', chat_views.delete_task, name='delete_task'),
    path('edit_task/<int:task_id>/', chat_views.edit_task, name='edit_task'),
]