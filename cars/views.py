from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404


# Create your views here.
from cars.models import Car


def cars(request):
    _cars = Car.objects.order_by('-created_date')
    paginator = Paginator(_cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    data = {
        'cars': paged_cars,
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

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            _cars = _cars.filter(description__icontains=keyword)

    data = {
        'cars': _cars,
    }

    return render(request, 'cars/search.html', data)
