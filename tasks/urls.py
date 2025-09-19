from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('view/', views.tasks_home, name='Tasks-home'),
    path(
        'delete_task/<int:task_id>/',
        views.delete_task, name='delete_task'
    ),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('addTask/', views.add_task, name='add_task'),
    path(
        'external_tasks/',
        views.external_tasks_home, name='External-tasks-home'
    ),
]
