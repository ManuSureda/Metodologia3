from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView

from .models import Property

# Create your views here.
class PropertyList(ListView):
    model = Property
    template_name = "index.html"

class PropertyCreate(CreateView):
    model = Property
    template_name = 'index.html'
    success_url = reverse_lazy('index')

class propertyReserveView(DetailView):
    model = Property
    template_name = 'reservation.html'



