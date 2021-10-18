from sqlite3 import IntegrityError

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render

from airport.forms import TrafficForm
from airport.models import Traffic


def home(request):
    message = "Welcome"
    return HttpResponse(message)


def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)


def listing(request):
    traffic_list = Traffic.objects.filter()
    paginator = Paginator(traffic_list, 100)
    page = request.GET.get('page')
    try:
        traffics = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        traffics = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        traffics = paginator.page(paginator.num_pages)
    context = {
        'traffics': traffics
    }
    return render(request, 'airport/listing.html', context)


def search(request):
    query = request.GET.get('query')
    if not query:
        traffics = Traffic.objects.all()
    else:
        traffics = Traffic.objects.filter(TERMINAL=query)
    if not traffics.exists():
        traffics = None
    title = "Résultats pour la requête %s" % query
    context = {
        'traffics': traffics,
    }
    return render(request, 'airport/search_form.html', context)

@transaction.atomic
def adding(request):
    if request.method == 'POST':
        form = TrafficForm(request.POST)
        if form.is_valid():
            DATA_EXTRACT_DATE = form.cleaned_data['DATA_EXTRACT_DATE']
            REPORT_PERIOD = form.cleaned_data['REPORT_PERIOD']
            TERMINAL = form.cleaned_data['TERMINAL']
            ARRIVAL_DEPARTURE = form.cleaned_data['ARRIVAL_DEPARTURE']
            DOMESTIC_INTERNATIONAL = form.cleaned_data['DOMESTIC_INTERNATIONAL']
            PASSENGER_COUNT = form.cleaned_data['PASSENGER_COUNT']
        try:
            with transaction.atomic():
                traffic = Traffic.objects.create(
                    DATA_EXTRACT_DATE=DATA_EXTRACT_DATE,
                    REPORT_PERIOD=REPORT_PERIOD,
                    TERMINAL=TERMINAL,
                    ARRIVAL_DEPARTURE=ARRIVAL_DEPARTURE,
                    DOMESTIC_INTERNATIONAL=DOMESTIC_INTERNATIONAL,
                    PASSENGER_COUNT=PASSENGER_COUNT
                    )
                context = {
                    'traffic_terminal': traffic.TERMINAL
                }
                return render(request, 'airport/merci.html', context)
        except IntegrityError:
            form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."
    else:
        form = TrafficForm()
    context = {
      'form': form
    }
    return render(request, 'airport/adding.html', context)