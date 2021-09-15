from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path

from testingapp.views import test, hello_world


urlpatterns = [
    path('test/', test),
    path('new/', hello_world),
]
