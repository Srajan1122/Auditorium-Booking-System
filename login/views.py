from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.conf import settings

Username=None;
user=None;
def loginpage(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        print(Username)
        user = authenticate(request, username=Username, password=Password)
        print(user)
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
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    elif request.user.is_authenticated and request.method == 'POST':
        logout(request)
        print(user,Username)
        loggedout = redirect('/loggedout/')
        return loggedout
    params={'pro':Username}
    return render(request, 'login/success.html',params)


def loggedout(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'login/loggedout.html')
