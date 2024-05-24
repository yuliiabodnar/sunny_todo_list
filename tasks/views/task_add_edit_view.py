# tasks/views/task_add_edit_view.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from tasks.models import Task
from tasks.forms.handlers.task_form_handler import handle_task_form


class TaskAddEditView(View):
    """
    A class-based view for adding and editing tasks.
    """
    template_name = 'tasks/task_add_edit.html' # Template to render the form

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
        Handle GET requests to display the form for adding or editing a task.

        Args:
            request (HttpRequest): The HTTP request object.
            task_id (int, optional): The ID of the task to edit. Defaults to None.

        Returns:
            HttpResponse: The rendered form.
        """
        task = self.get_task(pk)
        form, form_saved = handle_task_form(request, task)
        return self.render_form(request, form, task)

    def post(self, request, pk=None):
        """
        Handle POST requests to process the form for adding or editing a task.

        Args:
            request (HttpRequest): The HTTP request object.
            task_id (int, optional): The ID of the task to edit. Defaults to None.

        Returns:
            HttpResponseRedirect: Redirects to the task list view if the form is saved successfully.
            HttpResponse: The rendered form if the form is not valid.
        """
        task = self.get_task(pk)
        form, form_saved = handle_task_form(request, task)
        if form_saved:
            return redirect('tasks:task_list')
        return self.render_form(request, form, task)

    def render_form(self, request, form, task):
        """
        Render the form with the provided context.

        Args:
            request (HttpRequest): The HTTP request object.
            form (Form): The form to render.
            task (Task, optional): The task object, if any. Defaults to None.

        Returns:
            HttpResponse: The rendered form.
        """
        return render(request, self.template_name, {'form': form, 'task': task})
