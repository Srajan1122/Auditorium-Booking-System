from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.http import HttpResponse


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
    hi = request.user.username
    params = {'pro': hi}
    print ("id:",request.user.id)
    return render(request, 'login/Homepage.html', params)


def loggedout(request):
    if request.user.is_authenticated and request.method == 'POST':
        logout(request)
    return render(request, 'login/loggedout.html')


@login_required
def booking(request):
    if 'userid' in request.POST or request.method == "POST":
        form = BookingForm(request.POST,request = request)
        if form.is_valid:
            form.save()
        else:
            return HttpResponse('invail form')
    form = BookingForm(request = request )
    return render(request, 'login/Booking.html',{'form' : form})

@login_required
def Requests(request):
    return render(request, 'login/Requests.html')


@login_required
def History(request):
    return render(request, 'login/History.html')


def Register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.save()
        user = authenticate(request, username=username, password=password)
        login(request, user)
        response = redirect('/Homepage/')
        return response

    return render(request, 'login/register.html')
