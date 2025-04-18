from django.shortcuts import get_object_or_404
from django.utils.timezone import now, timedelta
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task
from .forms import RoomForm
from .models import Message, Room
from django.contrib import messages
# Create your views here.

@login_required()
def chat_home(request):
    messages.info(request, 'Refresh the page to see new messages.')
    form = RoomForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        room_name = form.cleaned_data['room_name']
        db_messages = Message.objects.filter(room=room_name)[:]
        username = request.user.username
        messages.success(request, f"Joined: {room_name}")
        return render(request, 'chat_and_tasks/chatroom.html', {'room_name': room_name, 'title': room_name, 'db_messages': db_messages, 'username': username})

    return render(request, 'chat_and_tasks/index.html', {'form': form})
