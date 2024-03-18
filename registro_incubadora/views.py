from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Registro
from . forms import RegistroForm


def inicio(request):
    return render(request, 'inicio.html')


def formulario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inicio.html')
    else:
        form = RegistroForm()
    return render(request, 'formulario.html', {'form': form})

def list_registro(_request):
    registro = list(Registro.objects.values())
    data = {'registro': registro}
    return JsonResponse(data)