"""
This file is for routing to the consumer
"""
from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat_and_tasks/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
