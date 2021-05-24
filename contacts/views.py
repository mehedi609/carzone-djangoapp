from django.shortcuts import render, redirect


# Create your views here.


def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']

        return redirect('/cars/'+car_id)
