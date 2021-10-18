from django.test import TestCase

from airport.models import Traffic


class TestAjoutTraffic(TestCase):
    def setUp(self):
        Traffic.objects.create(
            DATA_EXTRACT_DATE='2014-05-01T00:00:00.000',
            REPORT_PERIOD = '2018-05-01T00:00:00.000',
            TERMINAL = 'Roissy',
            ARRIVAL_DEPARTURE = 'Arrival',
            DOMESTIC_INTERNATIONAL = 'International',
            PASSENGER_COUNT = 12,
        )
        Traffic.objects.create(
            DATA_EXTRACT_DATE='2014-05-01T00:00:00.000',
            REPORT_PERIOD='2018-05-01T00:00:00.000',
            TERMINAL='Roissy',
            ARRIVAL_DEPARTURE='Arrivée',
            DOMESTIC_INTERNATIONAL='International',
            PASSENGER_COUNT=12,
        )

    def tearDown(self):
        Traffic.objects.all().delete()

    def test_new_traffic_is_registered(self):
        old_traffics = Traffic.objects.count()
        self.assertEqual(old_traffics,2)


    def test_new_traffic_data(self):
        data1 = Traffic.objects.get(pk=1)
        data2 = Traffic.objects.get(pk=2)
        self.assertEqual(data1.__str__(),'05/01/2014Arrival')
        self.assertEqual(data2.__str__(),'05/01/2014Arrivée')


    def test_delete_everything(self):
        Traffic.objects.all().delete()
        self.assertEqual(Traffic.objects.all(),0)