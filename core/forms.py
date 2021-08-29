from django.db.models import fields
from django.forms import ModelForm
from .models import Profissional, TipoDeProfissional


class ProfissionalForm(ModelForm):
    class Meta:
        model = Profissional
        fields = '__all__'


class TipoDeProfissionalForm(ModelForm):
    class Meta:
        model = TipoDeProfissional
        fields = '__all__'