# tasks/views/task_delete_view.py

from django.shortcuts import redirect, get_object_or_404
from django.views import View
from tasks.models.task import Task


class TaskDeleteView(View):
    def get_task(self, task_id):
        """
        Retrieve a task by its ID if provided, otherwise return None.

        Args:
            task_id (int): ID of the task to retrieve.

        Returns:
            Task: The task object if found, otherwise None.
        """
        if task_id:
            return get_object_or_404(Task, pk=task_id)
        return None

    def get(self, request, pk=None):
        """
        Handle HTTP GET request to delete a task.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int):              The primary key of the task to delete.

        Returns:
            HttpResponseRedirect: Redirects to the task list page after deletion.
        """
        # Retrieve the task object
        task = self.get_task(pk)

        # Delete the task
        task.delete()

        # Redirect to the task list page
        return redirect('tasks:task_list')
