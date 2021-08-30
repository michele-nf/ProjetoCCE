from django.urls import path, include
from .views import (
    home, 
    lista_profissional, 
    lista_tipo_de_profissional,
    profissional_novo,
    tipo_de_profissional_novo,
    profissional_update,
    tipo_de_profissional_update
)


urlpatterns = [
    path(r'', home, name='core_home'),
    #Profissional - Lista
    #core/profissional/
    path(r'profissional/', lista_profissional, name='core_lista_profissional'),
    #Profissional - Novo
    #core/profissional-novo
    path(r'profissional-novo/', profissional_novo, name='core_profissional_novo'),
    #Profissional - Update
    #core/profissional-update
    path(r'^profissional-update/(?P<id>\d+)/$', profissional_update, name='core_profissional_update'),
    #Tipo de profissional - Lista
    #core/tipo_de_profissional
    path(r'tipo_de_profissional/', lista_tipo_de_profissional, 
        name='core_lista_tipo_de_profissional'),
    #Tipo de profissional - Novo
    #core/tipo_de_profissioal-novo
    path(r'tipo_de_profissional-novo/', tipo_de_profissional_novo, name='core_tipo_de_profissional_novo'),
    #Tipo de Profissional - Update
    #core/tipo_de_profissional-update
    path(r'^tipo_de_profissional-update/(?P<id>\d+)/$', tipo_de_profissional_update, name='core_tipo_de_profissional_update'),
]