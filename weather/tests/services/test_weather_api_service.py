import unittest
from unittest.mock import patch
from weather.services.weather_api_service import WeatherAPIService


class TestWeatherAPIService(unittest.TestCase):
    def setUp(self):
        self.api_key = "your_api_key"
        self.weather_service = WeatherAPIService(self.api_key)

    @patch('urllib.request.urlopen')
    def test_get_weather_data_success(self, mock_urlopen):
        # Mock the response from the weather API
        mock_response = b'{"main": {"temp": 25}, "weather": [{"main": "Clear", "icon": "01d"}]}'
        mock_urlopen.return_value.read.return_value = mock_response

        # Call the method under test
        weather_data = self.weather_service.get_weather_data("London")

        # Verify the result
        self.assertEqual(weather_data, {'main': {'temp': 25}, 'weather': [{'main': 'Clear', 'icon': '01d'}]})

    @patch('urllib.request.urlopen')
    def test_get_weather_data_failure(self, mock_urlopen):
        # Mock an exception being raised during API call
        mock_urlopen.side_effect = Exception("API call failed")

        # Call the method under test
        weather_data = self.weather_service.get_weather_data("London")

        # Verify the result
        self.assertEqual(weather_data, {'error': 'API call failed'})


if __name__ == '__main__':
    unittest.main()