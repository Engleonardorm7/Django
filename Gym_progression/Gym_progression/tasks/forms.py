from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields =['date','weight','calories_consumed']
        widgets={
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Date'}),
            'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Record your weight'}),
            'calories_consumed': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Calories consumed this day'}),
        }