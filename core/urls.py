from django.urls import path, include
from .views import home, lista_profissional, lista_tipo_de_profissional


urlpatterns = [
    path(r'', home, name='core_home'),
    #Profissional
    #core/profissional/
    path(r'profissional/', lista_profissional, name='core_lista_profissional'),
    #Tipo de profissional
    #core/tipo_de_profissional
    path(r'tipo_de_profissional/', lista_tipo_de_profissional, 
        name='core_lista_tipo_de_profissional'),
]