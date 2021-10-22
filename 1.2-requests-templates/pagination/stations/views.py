from django.shortcuts import render, redirect
from django.urls import reverse
from csv import DictReader
from django.core.paginator import Paginator
from django.conf import settings

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as f:
        bus_list = list(DictReader(f))

    paginator = Paginator(bus_list, 10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
        'has_previous': page.previous_page_number() if page.has_previous() else 0,
        'has_next': page.next_page_number() if page.has_next() else 0
    }
    return render(request, 'stations/index.html', context)
