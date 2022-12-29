from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def index(request):
    task = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': 'title'})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html')
