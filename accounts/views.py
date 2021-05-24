from django.shortcuts import render, redirect

# Create your views here.


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        print('This is post method from register function')

    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    return redirect('home')
