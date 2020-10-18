from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from .forms import reserveForm
from .models import *

# Create your views here.
class PropertyList(ListView):
    model = Property
    template_name = "index.html"

class propertyReserveView(DetailView):
    model = Property
    form_class = reserveForm
    template_name = 'reservation.html'

class reserve(CreateView):
    model = Reservation
    form_class = reserveForm
    template_name = 'reservation.html'
    success_url = reverse_lazy('index')




