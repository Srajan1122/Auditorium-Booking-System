from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginpage, name="loginpage"),
    path("failed/", views.failed, name="failed"),
    path("Homepage/", views.success, name="success"),
    path("loggedout/", views.loggedout, name="logout"),
    path("booking/", views.booking, name="booking"),
    path("Requests/", views.Requests, name="Requests"),
    path("History/", views.History, name="History"),
    path("Register/", views.Register, name="Register"),
    path("user_admin/", views.user_admin, name="user_admin"),
]
