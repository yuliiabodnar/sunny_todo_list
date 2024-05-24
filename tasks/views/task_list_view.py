# tasks/views/task_list_view.py

from django.views.generic import ListView
from tasks.models import Task


class TaskListView(ListView):
    """
    A class-based view for displaying a list of tasks.
    """
    model = Task  # Specify the model to use for the list view
    template_name = 'tasks/task_list.html'  # Specify the template to render
    context_object_name = 'tasks'  # Name of the context variable to use in the template
