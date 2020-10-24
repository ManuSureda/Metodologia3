from datetime import datetime
from decimal import *

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


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
        # global dateFrom
        # dateFrom = request.POST['dateFrom']
        # global dateTo
        # dateTo = request.POST['dateTo']
        # return render(request, '../templates/filter.html', context)
        return render(request, '../templates/index.html', context)


def detail(request, id=0):
    if request.method == "GET":
        property = Property.objects.filter(id=id)
        rentalDates = RentalDate.objects.filter(property=id, reservation__isnull=True)
        return render(request, '../templates/reservation.html', {'property': property, 'rentalDates': rentalDates, })
    return redirect('/')


def checkAvailability(dFrom, dTo, idProperty):
    flag = True
    # dateFrom = datetime.strptime(dFrom, "%Y-%m-%d")
    # dateTo = datetime.strptime(dTo, "%Y-%m-%d")
    dateList = RentalDate.objects.filter(
        property=idProperty,
        # rentaldate__date__gte=dateFrom,
        # rentaldate__date__lte=dateTo
    ).distinct().order_by('id')
    print("esto es dateList")
    for rentalDate in dateList:
        print(rentalDate.reservation.email)
        print(rentalDate.date)
        print(rentalDate.property)
        if dFrom.date() >= rentalDate.date <= dTo.date():
            print("entre al if jeje --------------")
            if not rentalDate.reservation is None:
                flag = False

    return flag


def reserve(request, id=0):
    if request.method == "POST":
        print("-------------------------------------")
        for i in request.POST['dateList']:
            print(int(i))
        print("-------------------------------------")
        dateFrom = datetime.strptime(request.POST['dateFromR'], "%Y-%m-%d")
        dateTo = datetime.strptime(request.POST['dateToR'], "%Y-%m-%d")
        totalDaysStr = dateTo - dateFrom
        totalDays = str(totalDaysStr).split()[0]

        flag = checkAvailability(dateFrom, dateTo, id)

        print(flag)

        if not flag:
            print("entre al not flag")
            messages.add_message(request, messages.INFO, "the dates you have chosen has already been taken")
            return redirect('/detail/'+id)#mal

        property = Property.objects.get(id=id)

        getcontext().prec = 10  # no se que es

        totalCost = property.dailyCost * int(totalDays) + (property.dailyCost * int(totalDays)) * Decimal(1.08)

        name = request.POST['name']
        lastName = request.POST['lastName']
        email = request.POST['email']

        r = Reservation(property=property, name=name, lastName=lastName, email=email, totalCost=totalCost)
        r.save()

        datesList = RentalDate.objects.filter(property=id)
        for rentalDate in datesList:
            rentalDate.reservation = r
            rentalDate.save()

        print("aa")
        print("aa")
        print("aa")
        print("aa")
        print("aa")
        print("aa")
        print("aa")
        for rentalDate in datesList:
            print(rentalDate.property)
            print(rentalDate.reservation.email)
            print(rentalDate.date)


        print("aa")
        print("aa")
        print("aa")
        print("aa")
        print("aa")
        print("aa")
        print("aa")

        # for i in request.POST['date'].value():
        #     dte = int(i)
        #     rd = RentDate.objects.get(id=dte)
        #     rd.reservation = r
        #     rd.save()
        #     finalDates = RentDate.objects.filter(reservation=r.id)

        # reservationList = Reservation.objects.all()

        # print("esto es reservation list-------------------------------------------------------------------------------")
        # for res in reservationList:
        #     print(res.property)
        #     print(res.name)
        #     print(res.lastName)
        #     print(res.email)
        #     print(res.date)
        #     print(res.totalCost)

        # print(reservationList)
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
