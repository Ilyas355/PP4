from django.contrib import admin
from django.urls import path, include
from . import views as chat_views

urlpatterns = [
    path('', chat_views.chat_home, name='chat-home'),
    path('<str:room_name>/', chat_views.chat_room, name='chat-room'),
    path('chatroom/<int:id>', chat_views.delete_object_function, name='delete_object'),
]