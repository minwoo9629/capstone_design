from django import forms
from .models import Lecture

class LectureSettingForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['start_time','end_time','term','count']
        widgets = {
            'term': forms.Select(attrs={'class':'form-control'})
        }