import csv

from django.core.management.base import BaseCommand, CommandError

from airport.models import Traffic


class Command(BaseCommand):
    help = 'Load data in database'


    def handle(self, **options):
        try:
            with open('./data/data.csv', "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    print(row)
                    _, created = Traffic.objects.get_or_create(
                        DATA_EXTRACT_DATE=row[0],
                        REPORT_PERIOD=row[1],
                        TERMINAL=row[2],
                        ARRIVAL_DEPARTURE=row[3],
                        DOMESTIC_INTERNATIONAL=row[4],
                        PASSENGER_COUNT=row[5],
                    )
                    try:
                        created.save()
                    except:
                        print("nosaving")

        except FileNotFoundError as e:
            print("Pas de fichier :", e)