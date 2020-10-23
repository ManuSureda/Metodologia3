from datetime import datetime
from decimal import *

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from .forms import detailForm
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
        global dateFrom
        dateFrom = request.POST['dateFrom']
        global dateTo
        dateTo = request.POST['dateTo']
        # return render(request, '../templates/filter.html', context)
        return render(request, '../templates/index.html', context)


def detail(request, id=0):
    if request.method == "GET":
        property = Property.objects.filter(id=id)
        return render(request, '../templates/reservation.html', {'property': property, })
    return redirect('/')


def reserve(request, id=0):
    if request.method == "POST":
        print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        print(dateFrom)
        fecha1 = datetime.strptime(dateTo, "%Y-%m-%d")
        fecha2 = datetime.strptime(dateFrom, "%Y-%m-%d")
        totalDaysStr = fecha1 - fecha2
        totalDays = str(totalDaysStr).split()[0]
        print(totalDays)



        property = Property.objects.get(id=id)
        getcontext().prec = 10
        totalCost = property.dailyCost * int(totalDays) + (property.dailyCost * int(totalDays)) * Decimal(1.08)
        name = request.POST['name']
        lastName = request.POST['lastName']
        email = request.POST['email']

        r = Reservation(property=property, name=name, lastName=lastName, email=email, totalCost=totalCost)
        r.save()
        # propertyDates = RentalDate.objects.filter(property=property.id)
        # for i in propertyDates:
        #     dte = int(i)
        #     rd = RentalDate.objects.get(id=dte)
        #     rd.reservation = r
        #     rd.save()
        # finalDates = RentalDate.objects.filter(reservation=r.id)

        return render(request, '../templates/thanks.html',
                      {'property': property, 'reservation': r,
                       'total': round(r.totalCost, 2)}, )
    return redirect('/')

# class Reserve(CreateView):
#     model = Reservation
#     form_class = reserveForm
#     success_url = reverse_lazy('index')
#     template_name = 'reservation.html'
#
#     def form_valid(self, form):
#         form.instance.property = get_object_or_404(Property, id=self.kwargs.get('pk'))
#
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super(Reserve, self).get_context_data(**kwargs)
#         pk = self.kwargs['pk']
#         context['property'] = Property.objects.filter(pk=pk)
#         context['idProperty'] = pk
#         return context
