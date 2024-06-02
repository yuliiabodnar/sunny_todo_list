from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from tasks.models import Task
from locations.models import Location
from tasks.views.task_add_edit_view import TaskAddEditView
from unittest.mock import Mock, patch
from django.http import Http404


class TaskAddEditViewTest(TestCase):
    def setUp(self):
        # Set up a RequestFactory and sample data
        self.client = Client()
        self.factory = RequestFactory()
        self.location = Location.objects.create(name="Test Location")
        self.task = Task.objects.create(name="Test Task", location=self.location)
        self.view = TaskAddEditView()

    def test_get_task(self):
        # Test retrieving a task by ID
        request = self.factory.get(reverse('tasks:task_edit', kwargs={'pk': self.task.pk}))
        response = self.view.get(request, pk=self.task.pk)
        self.assertEqual(response.status_code, 200)

    def test_get_task_not_found(self):
        # Test retrieving a non-existing task
        request = self.factory.get(reverse('tasks:task_edit', kwargs={'pk': 999}))
        with self.assertRaises(Http404):
            self.view.get_task(999)

    def test_get(self):
        # Test GET request to display the form for editing a task
        request = self.factory.get(reverse('tasks:task_edit', kwargs={'pk': self.task.pk}))
        response = self.view.get(request, pk=self.task.pk)
        self.assertEqual(response.status_code, 200)

    def test_get_new_task(self):
        # Test GET request to display the form for adding a new task
        request = self.factory.get(reverse('tasks:task_add'))
        response = self.view.get(request)
        self.assertEqual(response.status_code, 200)

    @patch('tasks.handlers.forms.task_form_handler.handle_task_form')
    def test_post(self, mock_handle_task_form):
        # Test POST request to process the form for editing a task
        mock_handle_task_form.return_value = (Mock(), True)

        # Create a POST request
        url = reverse('tasks:task_edit', kwargs={'pk': self.task.pk})
        data = {
            'name': 'Updated Task',
            'location': self.location.id,
            'completed': False,
            'temperature': '20',
            'is_rain': False,
            'is_cloudy': False,
            'is_sunny': True
        }
        response = self.client.post(url, data)

        # Check the response
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tasks:task_list'))

    @patch('tasks.views.task_add_edit_view.handle_task_form')
    def test_post_invalid(self, mock_handle_task_form):
        # Test POST request with invalid data
        mock_handle_task_form.return_value = (Mock(), False)
        request = self.factory.post(reverse('tasks:task_edit', kwargs={'pk': self.task.pk}), {
            'name': '',
            'location': self.location.id
        })
        response = self.view.post(request, pk=self.task.pk)
        self.assertEqual(response.status_code, 200)