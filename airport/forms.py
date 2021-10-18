from django import forms
from django.forms import TextInput

from airport.models import Traffic


class TrafficForm(forms.Form):
    DATA_EXTRACT_DATE = forms.CharField(
        label='DATA_EXTRACT_DATE',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    REPORT_PERIOD = forms.CharField(
        label='REPORT_PERIOD',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    TERMINAL = forms.CharField(
        label='TERMINAL',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    ARRIVAL_DEPARTURE = forms.CharField(
        label='ARRIVAL_DEPARTURE',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    DOMESTIC_INTERNATIONAL = forms.CharField(
        label='DOMESTIC_INTERNATIONAL',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    PASSENGER_COUNT = forms.CharField(
        label='PASSENGER_COUNT',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

