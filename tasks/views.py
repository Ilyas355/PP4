from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.timezone import now, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task

# Create your views here.

def filter_option_function(filter, tasks):
    print(filter)
    if filter == "completed":
        return tasks.filter(complete=True)
    elif filter == "incomplete":
        return tasks.filter(complete=False)
    elif filter == "week":
        return tasks.filter(date_added__gte=now() - timedelta(days=7))
    elif filter== "month":
        return tasks.filter(date_added__gte=now() - timedelta(days=30))
    else:
        return tasks

@login_required()
def tasks_home(request):
    filter_option = request.GET.get("filter", "all")
    tasks = Task.objects.filter(name=request.user)
    tasks = filter_option_function(filter_option, tasks)
    print(request.user.username)


    return render(request, 'chat/Tasks.html', {'tasks': tasks, 'username': request.user.username, 'date_added': [task.date_added for task in tasks], 'selected_filter': filter_option})


@login_required()
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.delete()
    
    return redirect("Tasks-home")