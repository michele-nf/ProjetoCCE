from django.urls import path, include
from .views import home


urlpatterns = [
    path(r'', home, name='core_home'),
]