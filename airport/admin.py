from django.contrib import admin

# Register your models here.
from airport.models import Traffic


@admin.register(Traffic)
class TrafficAdmin(admin.ModelAdmin):
    model = Traffic
    # search_fields = ['passenger_count', 'terminal']
    list_filter = ['PASSENGER_COUNT', 'TERMINAL']
