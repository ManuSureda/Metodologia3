from django import forms
import datetime
from bootstrap_datepicker_plus import DateTimePickerInput

from .models import RentalDate


# class dateForm(forms):
#         dateFrom = forms.DateField(label="", input_formats=['%Y-%m-%d'], help_text="Desde",
#                                    widget=DateTimePickerInput(
#                                        format='%Y-%m-%d',
#                                        options={'minDate': (datetime.datetime.today().strftime("%Y-%m-%d"))}).start_of(
#                                        'event days'))
#         dateTo = forms.DateField(label="", input_formats=['%Y-%m-%d'], help_text="Hasta",
#                                  widget=DateTimePickerInput(format='%Y-%m-%d').end_of('event days'))


