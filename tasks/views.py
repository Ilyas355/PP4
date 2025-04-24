from django.shortcuts import render
from django.utils.timezone import now, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task

# Create your views here.


@login_required()
def tasks_home(request):

    return render(request, 'tasks/tasks.html')
