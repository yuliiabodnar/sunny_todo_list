from django.test import TestCase, RequestFactory
from django.contrib.messages.storage.fallback import FallbackStorage
from django.urls import reverse
from tasks.models import Task
from locations.models import Location
from tasks.middleware.check_task_completed_middleware import CheckTaskCompletedMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware


class MiddlewareTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = CheckTaskCompletedMiddleware(get_response=lambda x: None)
        self.location = Location.objects.create(name="Test Location")  # Create a Location object
        self.task = Task.objects.create(name="Test Task", completed=False,
                                        location=self.location)  # Provide location when creating Task
        # Add middleware to the test request
        self.request = self.factory.get(reverse('tasks:task_edit', kwargs={'pk': self.task.pk}))
        self.middleware(self.request)

        # Initialize session middleware
        session_middleware = SessionMiddleware()
        session_middleware.process_request(self.request)

        # Initialize message middleware
        message_middleware = MessageMiddleware()
        message_middleware.process_request(self.request)

        # Apply middleware to the request
        self.response = self.middleware(self.request)

    def test_task_edit_not_completed(self):
         # Apply middleware to the request
        response = self.middleware(self.request)

        # Check if the response is None (request passed through middleware)
        self.assertIsNone(response)

    def test_task_edit_completed(self):
        self.task.completed = True
        self.task.save()

        # Apply middleware to the request
        response = self.middleware(self.request)

        # Check if the response is a redirect
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('tasks:task_list'))
