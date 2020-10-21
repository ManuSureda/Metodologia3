from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name

class Property(models.Model):
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    maxPax = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    image = models.ImageField(upload_to='property', null=True)
    dailyCost = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title


class Reservation(models.Model):
    property = models.ForeignKey(Property, on_delete=models.PROTECT, blank=False, null=False)
    name = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    email = models.EmailField(max_length=200)
    dateFrom = models.DateField()
    dateTo = models.DateField()
    totalCost = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)

    class Meta:
        verbose_name_plural = 'Reservations'



class RentalDate(models.Model):
    date = models.DateField()
    property = models.ForeignKey(Property, null=True, on_delete=models.SET_NULL)
    reservation = models.ForeignKey(Reservation, null=True,  on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'RentalDates'
