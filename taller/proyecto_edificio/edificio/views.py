from django.shortcuts import render, redirect, get_object_or_404
from .models import Edificio, Departamento
from .forms import EdificioForm, DepartamentoForm

def lista_edificios(request):
    edificios = Edificio.objects.all()
    return render(request, 'edificios/lista_edificios.html', {'edificios': edificios})

def lista_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'departamentos/lista_departamentos.html', {'departamentos': departamentos})

def edificio_nuevo(request):
    if request.method == "POST":
        form = EdificioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(lista_edificios)
    else:
        form = EdificioForm()
    return render(request, 'edificios/edificio_form.html', {'form': form})

def edificio_editar(request, pk):
    edificio = get_object_or_404(Edificio, pk=pk)
    if request.method == "POST":
        form = EdificioForm(request.POST, instance=edificio)
        if form.is_valid():
            form.save()
            return redirect('lista_edificios')
    else:
        form = EdificioForm(instance=edificio)
    return render(request, 'edificios/edificio_form.html', {'form': form})

def edificio_eliminar(request, pk):
    edificio = get_object_or_404(Edificio, pk=pk)
    if request.method == "POST":
        edificio.delete()
        return redirect('lista_edificios')
    return render(request, 'edificios/edificio_confirmar_eliminar.html', {'edificio': edificio})

def departamento_nuevo(request):
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_edificios')
    else:
        form = DepartamentoForm()
    return render(request, 'edificios/departamento_form.html', {'form': form})

def departamento_editar(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == "POST":
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('lista_edificios')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'edificios/departamento_form.html', {'form': form})

def departamento_eliminar(request, pk):
    departamento = get_object_or_404(Departamento, pk=pk)
    if request.method == "POST":
        departamento.delete()
        return redirect('lista_edificios')
    return render(request, 'edificios/departamento_confirmar_eliminar.html', {'departamento': departamento})

"""

"""
from rest_framework import viewsets, permissions
from .serializers import EdificioSerializer, DepartamentoSerializer

class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
