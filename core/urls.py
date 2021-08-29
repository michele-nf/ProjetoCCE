from django.urls import path, include
from .views import (
    home, 
    lista_profissional, 
    lista_tipo_de_profissional,
    profissional_novo
)


urlpatterns = [
    path(r'', home, name='core_home'),
    #Profissional - Lista
    #core/profissional/
    path(r'profissional/', lista_profissional, name='core_lista_profissional'),
    #Profissional - Novo
    #core/profissional-novo
    path(r'profissional-novo', profissional_novo, name='core_profissional_novo'),
    #Tipo de profissional - Lista
    #core/tipo_de_profissional
    path(r'tipo_de_profissional/', lista_tipo_de_profissional, 
        name='core_lista_tipo_de_profissional'),

]