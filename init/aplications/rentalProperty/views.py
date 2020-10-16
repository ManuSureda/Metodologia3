from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Property

# Create your views here.
class PropertyList(ListView):
    model = Property
    template_name = "index.html"
