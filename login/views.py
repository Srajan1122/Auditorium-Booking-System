from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User


def loginpage(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            response = redirect('/success/')
            return response
        else:
            failedresponse = redirect('/failed/')
            return failedresponse
    return render(request, 'login/loginpage.html')


def failed(request):
    return render(request, 'login/failed.html')


def success(request):
    if request.method == 'POST':
        logout(request)
        loggedout = redirect('/loggedout/')
        return loggedout
    
    return render(request, 'login/success.html')


def loggedout(request):
    return render(request, 'login/loggedout.html')
