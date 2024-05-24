from tasks.models import Task
from ..task_form import TaskForm


def handle_task_form(request, task=None):
    """
    Handle task form logic.

    Args:
        request (HttpRequest): The incoming HTTP request.
        task (Task, optional): The Task instance to be edited. Defaults to None.

    Returns:
        tuple: A tuple containing the form instance and a boolean indicating if the form was valid and saved.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return form, True
    else:
        form = TaskForm(instance=task)

    return form, False
