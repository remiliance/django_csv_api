import unittest
from django.test import Client

from rest_framework.test import APITestCase
from rest_framework import status


class testAPI(unittest.TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('http://127.0.0.1:8000/airport/api/traffic/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
