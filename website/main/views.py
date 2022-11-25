from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>hello</h1>')


def findme(request):
    return render(request,'findme.html')


def about(request):
    return HttpResponse('<h1>Про нас</h1>')
