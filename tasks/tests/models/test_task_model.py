from django.test import TestCase
from tasks.models import Task
from locations.models import Location


class TaskModelTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.location = Location.objects.create(name="Test Location")

    def test_task_creation(self):
        """
        Test if a Task can be created and has the correct attributes.
        """
        task = Task.objects.create(
            name="Test Task",
            location=self.location,
            temperature='20',
            is_rain=True,
            is_cloudy=True,
            is_sunny=False
        )
        self.assertEqual(task.name, "Test Task")
        self.assertEqual(task.location, self.location)
        self.assertFalse(task.completed)
        self.assertEqual(task.temperature, '20')
        self.assertTrue(task.is_rain)
        self.assertTrue(task.is_cloudy)
        self.assertFalse(task.is_sunny)
        self.assertIsNotNone(task.created_at)

    def test_task_default_completed(self):
        """
        Test if the 'completed' field defaults to False.
        """
        task = Task.objects.create(name="Test Task", location=self.location)
        self.assertFalse(task.completed)

    def test_task_default_temperature(self):
        """
        Test if the 'temperature' field defaults to an empty string.
        """
        task = Task.objects.create(name="Test Task", location=self.location)
        self.assertEqual(task.temperature, '')

    def test_task_default_is_rain(self):
        """
        Test if the 'is_rain' field defaults to False.
        """
        task = Task.objects.create(name="Test Task", location=self.location)
        self.assertFalse(task.is_rain)

    def test_task_default_is_cloudy(self):
        """
        Test if the 'is_cloudy' field defaults to False.
        """
        task = Task.objects.create(name="Test Task", location=self.location)
        self.assertFalse(task.is_cloudy)

    def test_task_default_is_sunny(self):
        """
        Test if the 'is_sunny' field defaults to False.
        """
        task = Task.objects.create(name="Test Task", location=self.location)
        self.assertFalse(task.is_sunny)

    def test_task_str(self):
        """
        Test the string representation of the Task model.
        """
        task = Task.objects.create(name="Test Task", location=self.location)
        self.assertEqual(str(task), "Test Task")
