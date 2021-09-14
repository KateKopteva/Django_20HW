from django import forms
from .models import *

class AddForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields =['firstname', 'lastname', 'age', 'proffession']
