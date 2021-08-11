from django import forms
from django.db.models import fields
from django.forms.models import fields_for_model
from django.utils.regex_helper import Choice
from web_app.models import *

class Aspirante_Form(forms.ModelForm):

    class Meta:
        model = Aspirante
        fields = '__all__'
        labels = {
            'id_profesion': ('Profesion'),
            'id_agencia': ('Agencia'),
        }

class Oferta_Form(forms.ModelForm):

    class Meta:
        model = Oferta
        fields = '__all__'
        labels = {
            'nombre': ('Nombre oferta')
        }

class Empleabilidad_Form(forms.ModelForm):

    class Meta:
        model = Empleabilidad
        fields = ('id_aspirante', 'id_oferta', )
        labels = {
            'id_aspirante': ('Nombre aspirante'),
            'id_oferta': ('Nombre oferta'),
        }