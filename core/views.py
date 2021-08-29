from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Profissional, TipoDeProfissional

from .forms import ProfissionalForm


def home(request):
    context = {'mensagem': 'Ola mundo'}
    return render(request, 'core/index.html', context)


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


def lista_tipo_de_profissional(request):
    tipoDeProfissionais = TipoDeProfissional.objects.all()
    return render(request, 'core/lista_tipo_de_profissional.html', {
        'tipoDeProfissionais': tipoDeProfissionais})



