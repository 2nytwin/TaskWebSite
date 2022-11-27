from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('findme', views.findme),
    path ('about', views.about)
]
