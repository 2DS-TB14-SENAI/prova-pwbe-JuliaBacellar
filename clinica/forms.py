from django import forms
from .models import Medico

class Medico(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'especialidade', 'crm', 'email']
