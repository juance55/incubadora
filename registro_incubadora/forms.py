from django import forms
from . models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = [
            'fecha',
            'tiempo_encubacion',
            'tasa_mortalidad',
            'tasa_supervivencia',
            'evaluar_raza',
            'inversion',
        ]
