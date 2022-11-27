from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def findme(request):
    return render(request,'findme.html')


def about(request):
    return render(request, 'main/about.html')
