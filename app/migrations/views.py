from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Alumno, Nota, Asistencia
from .forms import LoginForm, NotaForm, AsistenciaForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def notas_view(request):
    notas = Nota.objects.filter(alumno=request.user.alumno)
    return render(request, 'notas.html', {'notas': notas})

@login_required
def asistencia_view(request):
    asistencia = Asistencia.objects.filter(alumno=request.user.alumno)
    return render(request, 'asistencia.html', {'asistencia': asistencia})

@login_required
def estadisticas_view(request):
    notas = Nota.objects.filter(alumno=request.user.alumno)
    asistencia = Asistencia.objects.filter(alumno=request.user.alumno)
    # Código para generar gráficos y estadísticas
    return render(request, 'estadisticas.html')