# chat/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Room, Message
from asgiref.sync import sync_to_async

from channels.testing import WebsocketCommunicator
from channels.layers import get_channel_layer
from productivity_app.asgi import application  # Adjust if your project name is different
import json
import asyncio

class ChatViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.room = Room.objects.create(name='Test Room', slug='test-room')

    def test_chat_home_get(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('chat-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/index.html')

    def test_chat_home_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('chat-home'), {'room_name': self.room.slug})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/chatroom.html')
        self.assertContains(response, self.room.slug)

    def test_chat_room_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('chat-room', args=[self.room.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/chatroom.html')
        self.assertContains(response, self.room.slug)

    def test_delete_object_function(self):
        self.client.login(username='testuser', password='testpass')
        message = Message.objects.create(
            username='testuser', room=self.room.slug,
            message_content='Test message', profile_pic='profile.jpg'
        )
        response = self.client.get(reverse('delete_object', args=[message.id]))
        self.assertRedirects(response, '/')
        self.assertFalse(Message.objects.filter(id=message.id).exists())

class ChatConsumerTests(TestCase):
    async def test_websocket_connect_authenticated(self):
        user = await sync_to_async(User.objects.create_user)(
            username='asyncuser', password='testpass'
        )
        room = await sync_to_async(Room.objects.create)(
            name='Async Room', slug='async-room'
        )

        communicator = WebsocketCommunicator(
            application,
            f"/ws/chat/{room.slug}/"
        )
        communicator.scope['user'] = user
        communicator.scope['url_route'] = {'kwargs': {'room_name': room.slug}}

        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        await communicator.disconnect()

    async def test_websocket_send_and_receive_message(self):
        user = await sync_to_async(User.objects.create_user)(
            username='asyncuser', password='testpass'
        )
        room = await sync_to_async(Room.objects.create)(
            name='Async Room', slug='async-room'
        )

        communicator = WebsocketCommunicator(
            application,
            f"/ws/chat/{room.slug}/"
        )
        communicator.scope['user'] = user
        communicator.scope['url_route'] = {'kwargs': {'room_name': room.slug}}

        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        message = {
            "message": "Hello World",
            "username": user.username,
            "profile_pic": "profile.jpg",
            "room": room.slug
        }
        await communicator.send_json_to(message)

        response = await communicator.receive_json_from()
        self.assertEqual(response['message'], "Hello World")
        self.assertEqual(response['username'], user.username)
        self.assertEqual(response['room'], room.slug)

        await communicator.disconnect()
