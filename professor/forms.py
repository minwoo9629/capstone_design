from django import forms
from .models import Professor
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class FindDateForm(forms.Form):
    find_date = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'type':'date'}))

