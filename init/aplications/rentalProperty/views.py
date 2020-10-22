from django.db.models import QuerySet
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from .forms import reserveForm
from .models import *


# Create your views here.
def index(request):
    cities = City.objects.all()
    if 'filter' in request.GET:
        filterProperty = Property.objects.all().filter(city=request.GET['idCity'])
        context = {
            'properties': filterProperty,
            'cities': cities
        }
        return render(request, '../templates/index.html', context)
    else:
        properties = Property.objects.all()
        context = {
            'properties': properties,
            'cities': cities
        }
        return render(request, '../templates/index.html', context)


def filter(request):
    cities = City.objects.all()
    if request.method == 'POST':
        filterProperty = Property.objects.all().filter(
            city=request.POST['idCity'],
            rentaldate__date__gte=request.POST['dateFrom'],
            rentaldate__date__lte=request.POST['dateTo'],
            rentaldate__reservation__isnull=True,
            maxPax__gte=request.POST['passengers']).distinct().order_by('id')
        context = {
            'properties': filterProperty,
            'cities': cities,

        }
        return render(request, '../templates/filter.html', context)


class Reserve(CreateView):
    model = Reservation
    form_class = reserveForm
    success_url = reverse_lazy('index')
    template_name = 'reservation.html'

    def form_valid(self, form):
        form.instance.property = get_object_or_404(Property, id=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Reserve, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['property'] = Property.objects.filter(pk=pk)
        context['idProperty'] = pk
        return context
