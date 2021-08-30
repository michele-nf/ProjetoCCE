from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Profissional, TipoDeProfissional

from .forms import ProfissionalForm, TipoDeProfissionalForm


def home(request):
    return render(request, 'core/index.html')


def lista_profissional(request):
    profissionais = Profissional.objects.all()
    form = ProfissionalForm()
    data = {'profissionais': profissionais, 'form': form}
    return render(request, 'core/lista_profissional.html', data)    


def profissional_novo(request):
    form = ProfissionalForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_profissional')


def profissional_update(request, id):
    data = {}
    profissional = Profissional.objects.get(id=id)
    form = ProfissionalForm(request.POST or None, instance=profissional)
    data['profissional'] = profissional
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_profissional')
    else: 
        return render(request, 'core/profissional_update.html', data) 


def profissional_delete(request, id):
    profissional = Profissional.objects.get(id=id)
    if request.method == 'POST':
        profissional.delete()
        return redirect('core_lista_profissional')
    else:
        return render(request, 'core/profissional_delete.html', {'profissional': profissional})   


def lista_tipo_de_profissional(request):
    tipoDeProfissionais = TipoDeProfissional.objects.all()
    form = TipoDeProfissionalForm()
    data = {'tipoDeProfissionais': tipoDeProfissionais, 'form': form}
    return render(request, 'core/lista_tipo_de_profissional.html', data)


def tipo_de_profissional_novo(request):
    form =TipoDeProfissionalForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_tipo_de_profissional')


def tipo_de_profissional_update(request, id):
    data = {}
    tipoDeProfissional = TipoDeProfissional.objects.get(id=id)
    form = TipoDeProfissionalForm(request.POST or None, instance=tipoDeProfissional)
    data['tipoDeProfissional'] = tipoDeProfissional
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_tipo_de_profissional')
    else: 
        return render(request, 'core/tipo_de_profissional_update.html', data)


def tipo_de_profissional_delete(request, id):
    tipoDeProfissional = TipoDeProfissional.objects.get(id=id)
    if request.method == 'POST':
        tipoDeProfissional.delete()
        return redirect('core_lista_tipo_de_profissional')
    else:
        return render(request, 'core/tipo_de_profissional_delete.html', 
            {'tipoDeProfissional': tipoDeProfissional})
