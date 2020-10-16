from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import City

# Create your views here.
class CityList(ListView):
    model = City
    template_name = 'index.html'

