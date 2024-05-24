from django.shortcuts import render
from .models import Task, Location


# Create your views here.
def list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
