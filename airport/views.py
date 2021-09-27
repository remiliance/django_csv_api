from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

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