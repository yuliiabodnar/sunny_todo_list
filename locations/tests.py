import os
import django
from django.test import TestCase

import unittest
from unittest.mock import Mock, patch
from locations.weather.weather_service import WeatherService
from locations.weather.weather_parser import WeatherParser
from locations.weather.weather import Weather

# Ensure settings are configured
os.environ['DJANGO_SETTINGS_MODULE'] = 'sunny_todo_list.settings'
django.setup()


class TestWeatherService(unittest.TestCase):
    @patch('locations.weather.weather_service.requests.get')
    def test_get_weather_info_success(self, mock_get):
        # Create a mock request object
        mock_request = Mock()
        mock_request.scheme = 'https'
        mock_request.get_host.return_value = 'example.com'

        # Mock successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'temp': 20, 'main': 'Clear', 'icon': '01d'}
        mock_get.return_value = mock_response

        # Create a WeatherService instance
        weather_service = WeatherService(mock_request)

        # Test get_weather_info method
        weather_data = weather_service.get_weather_info('London')

        # Verify the result
        self.assertEqual(weather_data, {'temp': 20, 'main': 'Clear', 'icon': '01d'})

    @patch('locations.weather.weather_service.requests.get')
    def test_get_weather_info_failure(self, mock_get):
        # Create a mock request object
        mock_request = Mock()
        mock_request.scheme = 'https'
        mock_request.get_host.return_value = 'example.com'

        # Mock unsuccessful response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Create a WeatherService instance
        weather_service = WeatherService(mock_request)

        # Test get_weather_info method
        weather_data = weather_service.get_weather_info('London')

        # Verify the result
        self.assertIsNone(weather_data)


class TestWeatherParser(unittest.TestCase):
    def test_parse_location_weather_response(self):
        # Test successful parsing
        weather_parser = WeatherParser()
        weather_data = {'temp': 20, 'main': 'Clear', 'icon': '01d'}
        parsed_weather = weather_parser.parse_location_weather_response('London', weather_data)

        # Verify the result
        self.assertIsInstance(parsed_weather, Weather)
        self.assertEqual(parsed_weather.location, 'London')
        self.assertEqual(parsed_weather.temperature, 20)
        self.assertFalse(parsed_weather.is_rain)
        self.assertFalse(parsed_weather.is_cloudy)
        self.assertTrue(parsed_weather.is_sunny)

        # Test parsing with missing data
        with self.assertRaises(ValueError):
            weather_parser.parse_location_weather_response('London', None)


if __name__ == '__main__':
    unittest.main()