from django.urls import path
from .views import login_view, home_view, notas_view, asistencia_view, estadisticas_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    path('notas/', notas_view, name='notas'),
    path('asistencia/', asistencia_view, name='asistencia'),
    path('estadisticas/', estadisticas_view, name='estadisticas'),
]