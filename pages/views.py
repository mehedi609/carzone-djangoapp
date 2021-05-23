from django.shortcuts import render

from cars.models import Car
from pages.models import Team
from utils.helpers import get_search_fields


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')

    search_fields_dic = get_search_fields()

    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': search_fields_dic['model_search'],
        'city_search': search_fields_dic['city_search'],
        'year_search': search_fields_dic['year_search'],
        'body_style_search': search_fields_dic['body_style_search'],
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')