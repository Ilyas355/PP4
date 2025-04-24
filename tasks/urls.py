from django.contrib import admin
from django.urls import path, include
from . import views as chat_views

urlpatterns = [
    path('/', chat_views.tasks_home, name='Tasks-home'),
    path('delete_task/<int:task_id>/', chat_views.delete_task, name='delete_task'),
    path('edit_task/<int:task_id>/', chat_views.edit_task, name='edit_task'),
    path('addTask/', chat_views.add_task, name='add_task'),
    path('external_tasks/', chat_views.external_tasks_home, name='External-tasks-home'),
]