# tasks/views/task_list_view.py
from django.views.generic import ListView
from tasks.models.task import Task
from tasks.handlers.views.context_handler import update_tasks_if_completed
from django.template.response import TemplateResponse


class TaskListView(ListView):
    """
    A class-based view for displaying a list of tasks.
    """
    template_name = 'tasks/task_list.html'  # Specify the template to render

    def get(self, request):
        """
        Handle GET requests to display the task list.

        Args:
            request (HttpRequest): The HTTP GET request object.

        Returns:
            TemplateResponse: The rendered task list template.
        """
        tasks = Task.objects.all()
        updated_tasks = update_tasks_if_completed(tasks)

        return TemplateResponse(request, self.template_name, {'tasks': updated_tasks})
        
