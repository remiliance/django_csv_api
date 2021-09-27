from rest_framework import serializers

from airport import models


class TrafficSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Traffic
        fields = '__all__'
