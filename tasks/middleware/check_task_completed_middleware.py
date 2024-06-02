# myapp/middleware/check_task_completed_middleware.py

from django.shortcuts import redirect
from django.urls import reverse, resolve
from django.contrib import messages
from tasks.models import Task


class CheckTaskCompletedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Resolve the URL to get the view and arguments
        resolver_match = resolve(request.path)

        if resolver_match.view_name == 'tasks:task_edit':
            task_id = resolver_match.kwargs.get('pk')
            if task_id:
                try:
                    task = Task.objects.get(pk=task_id)
                    if task.completed:
                        messages.warning(request, "You cannot edit a completed task.")
                        return redirect('tasks:task_list')
                except Task.DoesNotExist:
                    messages.error(request, "Task does not exist.")
                    return redirect('tasks:task_list')

        response = self.get_response(request)
        return response
