from django.db.models import fields
from django.forms import ModelForm
from .models import Profissional


class ProfissionalForm(ModelForm):
    class Meta:
        model = Profissional
        fields = '__all__'