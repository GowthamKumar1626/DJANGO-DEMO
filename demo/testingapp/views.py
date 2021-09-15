from django.http.response import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("<h1>Hello Vihas</h1>")
    
def hello_world(request):
    return HttpResponse("<h1>Hello FARMX AI. Welcome to team</h1>")
