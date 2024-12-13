from django import forms
from .models import Alumno, Nota, Asistencia

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ('materia', 'nota')

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ('materia', 'fecha', 'asistio')
        
        