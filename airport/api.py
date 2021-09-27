from rest_framework import viewsets

from airport.models import Traffic
from airport.serializer import TrafficSerializer


class ApiTraffic(viewsets.ModelViewSet):
    """
    API endpoint that allows Traffic to be viewed or edited.
    """
    queryset = Traffic.objects.all()
    serializer_class = TrafficSerializer
