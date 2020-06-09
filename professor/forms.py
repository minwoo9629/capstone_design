from django import forms
from .models import Professor
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
class DateInput(forms.DateInput):
    input_type = 'date'

class FindDateForm(forms.Form):
    find_date = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'type':'date'}))