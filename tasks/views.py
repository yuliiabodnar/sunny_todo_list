from django.shortcuts import render, redirect,  get_object_or_404
from .models import Task, Location
from .forms.task_form import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_view(request, task_id):
    task = get_object_or_404(Task,  pk=task_id)
    return render(request, 'tasks/task_view.html', {'task': task})


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_add.html', {'form': form})
