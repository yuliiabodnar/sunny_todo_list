from django.shortcuts import render, redirect
from .models import Task, Location
from .forms.task_form import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_add.html', {'form': form})
