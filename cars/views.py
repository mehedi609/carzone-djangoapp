from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404


# Create your views here.
from cars.models import Car
from utils.helpers import get_search_fields


def cars(request):
    _cars = Car.objects.order_by('-created_date')
    paginator = Paginator(_cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    search_fields_dic = get_search_fields()

    data = {
        'cars': paged_cars,
        'model_search': search_fields_dic['model_search'],
        'city_search': search_fields_dic['city_search'],
        'year_search': search_fields_dic['year_search'],
        'body_style_search': search_fields_dic['body_style_search'],
    }

    return render(request, 'cars/cars.html', data)


def car_detail(request, _id):
    single_car = get_object_or_404(Car, pk=_id)

    data = {
        'single_car': single_car,
    }

    return render(request, 'cars/car_detail.html', data)


def search(request):
    _cars = Car.objects.order_by('-created_date')

    search_fields_dic = get_search_fields()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            _cars = _cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            _cars = _cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            _cars = _cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            _cars = _cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            _cars = _cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            _cars = _cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': _cars,
        'model_search': search_fields_dic['model_search'],
        'city_search': search_fields_dic['city_search'],
        'year_search': search_fields_dic['year_search'],
        'body_style_search': search_fields_dic['body_style_search'],
        'transmission_search': search_fields_dic['transmission_search'],
    }

    return render(request, 'cars/search.html', data)
