import unittest
import unittest.mock

import requests
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTest(unittest.TestCase):

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'countryName': 'United States of America',
            'cityName': 'Mountain View',
            'regionName': 'California'
        }
        
        result = get_location("8.8.8.8")
        self.assertEqual(
            result.get('country'),
            'United States of America'
        )
        
        mock_get.assert_called_once_with(
            'https://freeipapi.com/api/json/{}'.format('8.8.8.8')
        )
        
    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json= lambda: {
                    'countryName': 'United States of America',
                    'cityName': 'Mountain View',
                    'regionName': 'California'
                }
            ),
        ]
        
        with self.assertRaises( requests.exceptions.RequestException ):
            get_location("8.8.8.8")
            
        result = get_location("8.8.8.8")
       
        self.assertEqual(
            result.get('country'),
            'United States of America'
        )
        
        # mock_get.assert_called_once_with(
        #     'https://freeipapi.com/api/json/{}'.format('8.8.8.8')
        # )
        