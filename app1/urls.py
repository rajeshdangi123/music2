from django.urls import path
from app1 import views
from django.http import HttpResponse


urlpatterns = [
    path("", views.home, name="home"),
    path("singup1/", views.singup1, name="singup1"),
    path("login1/", views.login1, name="login1"),
    path("log_out/", views.log_out, name="log_out"),
    path("read/", views.read, name="read"),
    path('upload/',views.upload,name="upload"),
]
