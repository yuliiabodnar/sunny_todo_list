# tasks/tests/views/test_task_detail_view.py

from django.test import TestCase
from django.urls import reverse
from tasks.models import Task
from locations.models import Location


class TaskDetailViewTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(name="Test Location")
        self.task = Task.objects.create(name="Test Task", location=self.location, completed=False)

    def test_task_detail_view(self):
        # Get the URL for the task detail view
        url = reverse('tasks:task_detail', kwargs={'pk': self.task.pk})

        # Get the response
        response = self.client.get(url)

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if the task name is present in the response content
        self.assertContains(response, self.task.name)
