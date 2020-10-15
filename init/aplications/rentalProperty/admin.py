from django.contrib import admin
from .models import City,Property,RentalDate,Reservation
# Register your models here.
admin.site.register(City)
admin.site.register(Property)
admin.site.register(RentalDate)
admin.site.register(Reservation)