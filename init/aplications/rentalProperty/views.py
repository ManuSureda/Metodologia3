from datetime import datetime
from decimal import *
from random import random
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout, authenticate
from django.shortcuts import render, redirect
from .models import *
import random
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def index(request):
    cities = City.objects.all()
    properties = Property.objects.filter(rentaldate__date__gte=datetime.now(),
                                         rentaldate__reservation__isnull=True).distinct().order_by('id')
    context = {
        'properties': properties,
        'cities': cities
    }
    return render(request, '../templates/index.html', context)


def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "../templates/register.html", {'form': form})


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                do_login(request, user)
                print('entro')
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "../templates/login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')


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
        return render(request, '../templates/index.html', context)


def detail(request, id=0):
    if request.method == "GET":
        property = Property.objects.filter(id=id)
        rentalDates = RentalDate.objects.filter(property=id, reservation__isnull=True, date__gte=datetime.now())
        return render(request, '../templates/reservation.html', {'property': property, 'rentalDates': rentalDates, })
    return redirect('/')


def reserve(request, id=0):
    if request.method == "POST":

        property = Property.objects.get(id=id)

        listOfDays = request.POST.getlist('dateList')
        amountOfDays = len(listOfDays)
        totalCost = property.dailyCost * amountOfDays + (property.dailyCost * amountOfDays) * Decimal(1.08)

        name = request.POST['name']
        lastName = request.POST['lastName']
        email = request.POST['email']

        r = Reservation(property=property, name=name, lastName=lastName, email=email, totalCost=totalCost, code=random.randrange(999, 99999))
        r.save()

        for idRentalDate in listOfDays:
            RentalDate.objects.filter(id=idRentalDate).update(reservation=r)


        return render(request, '../templates/thanks.html',
                      {'property': property, 'reservation': r,
                       'total': round(r.totalCost, 2)}, )
    return redirect('/')

