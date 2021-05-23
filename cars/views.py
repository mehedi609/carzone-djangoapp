from django.shortcuts import render, get_object_or_404


# Create your views here.
from cars.models import Car


def cars(request):
    _cars = Car.objects.order_by('-created_date')

    data = {
        'cars': _cars,
    }

    return render(request, 'cars/cars.html', data)


def car_detail(request, _id):
    single_car = get_object_or_404(Car, pk=_id)

    data = {
        'single_car': single_car,
    }

    return render(request, 'cars/car_detail.html', data)


def search(request):
    return 'search'
