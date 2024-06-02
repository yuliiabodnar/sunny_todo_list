# tasks/tests/views/test_task_list_view.py

from django.test import TestCase, RequestFactory
from django.urls import reverse
from tasks.models import Task
from locations.models import Location
from tasks.views.task_list_view import TaskListView


class TaskListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.location = Location.objects.create(name="Test Location")
        self.task1 = Task.objects.create(name="Task 1", completed=True, location=self.location, temperature="25.0")
        self.task2 = Task.objects.create(name="Task 2", completed=False, location=self.location)

    def test_task_list_view(self):
        # Create a request
        request = self.factory.get(reverse('tasks:task_list'))

        # Call the TaskListView as a view
        response = TaskListView.as_view()(request)

        # Check if the correct template is used
        self.assertEqual(response.status_code, 200)

        # Check if the rendered content contains task names
        self.assertContains(response, 'Task 1')
        self.assertContains(response, 'Task 2')

        # Check if 'tasks' is in the context data
        self.assertTrue('tasks' in response.context_data)

        tasks_count = Task.objects.count()
        test_tasks = response.context_data['tasks']
        self.assertEqual(len(test_tasks), tasks_count)

        # Check if completed task has background class
        self.assertTrue(hasattr(test_tasks[0], 'background_class'))

        # Check if non-completed task doesn't have additional context data
        self.assertFalse(hasattr(test_tasks[1], 'background_class'))
