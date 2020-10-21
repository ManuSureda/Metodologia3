from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView

from .models import *


# Create your views here.
class PropertyList(ListView):
    model = Property
    template_name = "index.html"


class Reserve(CreateView):
    # context_object_name = 'property'
    model = Reservation
    fields = ['name', 'lastName', 'email', 'dateFrom', 'dateTo', 'totalCost']
    success_url = reverse_lazy('index')
    template_name = 'reservation.html'

    # form_class = reserveForm

    def form_valid(self, form):
        form.instance.property = get_object_or_404(Property, id=self.kwargs.get('pk'))  # new line
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Reserve, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['property'] = Property.objects.filter(pk=pk)
        context['idProperty'] = pk
        return context
