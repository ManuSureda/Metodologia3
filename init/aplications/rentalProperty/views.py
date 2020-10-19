from django.http import HttpResponseRedirect
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

    def get_context_data(self, **kwargs):
        context = super(reserve, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['property'] = Property.objects.filter(pk=pk)
        context['idProperty'] = pk
        return context






