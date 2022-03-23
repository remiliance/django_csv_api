"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import csv

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from airport import views



# pour charger les données depuis le data.sql dans la postgres
"""
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


"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('airport/', include('airport.urls', namespace='airport')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
