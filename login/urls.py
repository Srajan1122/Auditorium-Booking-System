from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginpage, name="loginpage"),
    path("failed/", views.failed, name="failed"),
    path("success/", views.success, name="success"),
    path("loggedout/", views.loggedout, name="logout"),

]
