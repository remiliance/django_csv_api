import unittest
from unittest import TestCase

from django.test import Client
from django.urls import reverse

from airport.models import Traffic


class ViewsTesting (unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        Traffic.objects.create(
            DATA_EXTRACT_DATE='2014-05-01T00:00:00.000',
            REPORT_PERIOD='2018-05-01T00:00:00.000',
            TERMINAL='Roissy',
            ARRIVAL_DEPARTURE='Arrival',
            DOMESTIC_INTERNATIONAL='International',
            PASSENGER_COUNT=1312122,
        )

    def test_index_launch(self):
        # Issue a GET request.
        response = self.client.get('/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


    def test_view_all_traffics(self):
        response = self.client.get('http://127.0.0.1:8000/airport/listing/')
        self.assertEqual(response.status_code, 200)
        # 2 au lancement
        old_traffics = Traffic.objects.count()
        self.assertEqual(self, old_traffics, 2) # mystere pkoi 2?


class IndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('/'))
        self.assertEqual(response.status_code, 200)