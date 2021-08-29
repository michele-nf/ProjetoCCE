from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Profissional, TipoDeProfissional


def home(request):
    context = {'mensagem': 'Ola mundo'}
    return render(request, 'core/index.html', context)


def lista_profissional(request):
    profissionais = Profissional.objects.all()
    return render(request, 'core/lista_profissional.html', {
        'profissionais': profissionais})


def lista_tipo_de_profissional(request):
    tipoDeProfissionais = TipoDeProfissional.objects.all()
    return render(request, 'core/lista_tipo_de_profissional.html', {
        'tipoDeProfissionais': tipoDeProfissionais})