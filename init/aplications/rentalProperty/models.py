from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class City(models.Model):
    idCity = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Property(models.Model):
    idProperty = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    maxPax = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    image = models.ImageField(upload_to='property')
    dailyCost = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title


class RentalDate(models.Model):
    idRentalDate = models.AutoField(primary_key=True)
    dateFrom = models.DateField()
    dateTo = models.DateField()
    property = models.ForeignKey(Property, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'RentalDates'


class Reservation(models.Model):
    idReservation = models.AutoField(primary_key=True)
    property = models.ForeignKey(Property, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length = 120)
    lastName = models.CharField(max_length=120)
    email = models.EmailField(max_length = 200)
    dateFrom = models.DateField()
    dateTo = models.DateField()
    totalCost = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)

    class Meta:
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.email
