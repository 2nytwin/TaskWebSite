from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h4>Hello</h4>')


def findme(request):
    return HttpResponse('<h1>Find me -_-</h1>')