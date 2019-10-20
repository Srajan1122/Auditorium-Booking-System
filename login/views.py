from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required


def loginpage(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        print(Username)
        temp = Username
        user = authenticate(request, username=Username, password=Password)
        print(user)
        if user is not None:
            login(request, user)
            response = redirect('/Homepage/')
            return response
        else:
            failedresponse = redirect('/failed/')
            return failedresponse
    return render(request, 'login/loginpage.html')


def failed(request):
    return render(request, 'login/failed.html')


def success(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    elif request.user.is_authenticated and request.method == 'POST':
        logout(request)
        loggedout = redirect('/loggedout/')
        return loggedout
    hi = request.user.username
    params = {'pro': hi}
    return render(request, 'login/Homepage.html', params)


def loggedout(request):
    return render(request, 'login/loggedout.html')


@login_required
def booking(request):
    if request.user.is_authenticated and request.method == 'POST':
        logout(request)
        loggedout = redirect('/loggedout/')
        return loggedout
    return render(request, 'login/Booking.html')


@login_required
def pending(request):

    if request.user.is_authenticated and request.method == 'POST':
        logout(request)
        loggedout = redirect('/loggedout/')
        return loggedout
    return render(request, 'login/pending.html')


@login_required
def History(request):
    if request.user.is_authenticated and request.method == 'POST':
        logout(request)
        loggedout = redirect('/loggedout/')
        return loggedout
    return render(request, 'login/History.html')
