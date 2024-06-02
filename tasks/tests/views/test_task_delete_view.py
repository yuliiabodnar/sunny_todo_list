from django.test import TestCase, RequestFactory
from django.urls import reverse
from locations.models import Location
from tasks.models import Task
from tasks.views import TaskDeleteView


class TaskDeleteViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.location = Location.objects.create(name="Test Location")
        self.task = Task.objects.create(name="Test Task", location=self.location)
        self.delete_url = reverse('tasks:task_delete', kwargs={'pk': self.task.pk})

    def test_get_confirm_delete(self):
        response = self.client.get(self.delete_url)
        self.assertContains(response, f'Are you sure you want to delete the task "{self.task.name}"?')

    def test_post_delete(self):
        request = self.factory.post(self.delete_url)
        response = TaskDeleteView.as_view()(request, pk=self.task.pk)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('tasks:task_list'))
