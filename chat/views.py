from django.shortcuts import get_object_or_404
from django.utils.timezone import now, timedelta
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RoomForm
from .models import Message, Room
from django.contrib import messages
# Create your views here.


@login_required()
def chat_home(request):
    form = RoomForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        room_name = form.cleaned_data['room_name']
        db_messages = Message.objects.filter(room=room_name)[:]
        username = request.user.username
        messages.success(request, f"Joined: {room_name}")
        return render(
            request,
            'chat/chatroom.html',
            {
                'room_name': room_name,
                'db_messages': db_messages,
                'username': username
            }
        )

    return render(request, 'chat/index.html', {'form': form})


@login_required
def chat_room(request, room_name):
    db_messages = Message.objects.filter(room=room_name)[:]
    username = request.user.username
    messages.success(request, f"Joined: {room_name}")
    return render(request, 'chat/chatroom.html', {
        'room_name': room_name,
        'title': room_name,
        'db_messages': db_messages,
        'username': username,
    })


@login_required
def delete_object_function(request, id):
    ob = Message.objects.filter(id=id)
    ob.delete()
    return redirect('/')
