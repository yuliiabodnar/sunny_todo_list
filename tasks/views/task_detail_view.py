# tasks/views/task_detail_view.py

from django.views.generic import DetailView
from tasks.models import Task


class TaskDetailView(DetailView):
    """
    A class-based view for displaying the details of a specific task.
    """
    model = Task  # Specify the model to use
    template_name = 'tasks/task_detail.html'  # Specify the template to render
    context_object_name = 'task'  # Name of the context variable to use in the template
