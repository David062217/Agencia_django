from ast import Str
import django
from django.db.models.query import QuerySet
from django.db.models.sql.query import Query
from django.http import request
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.utils.regex_helper import contains
from web_app.models import *
from .forms import *
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.utils import timezone
from datetime import time, timedelta

# Create your views here.

def home(request):
    return render(request, 'home.html')

def candidate(request):
    aspirantes = Aspirante.objects.all()
    return render(request, 'candidate.html',{'aspirantes':aspirantes})

class Create_candidato(CreateView):
    model = Aspirante
    form_class = Aspirante_Form
    template_name = 'register_candidate.html'
    success_url = reverse_lazy("register")

class Create_ofert(CreateView):
    model = Oferta
    form_class = Oferta_Form
    template_name = 'ofert.html'
    success_url = reverse_lazy("home")

def oferts(request):
    today = timezone.now() - timedelta(days=5)
    oferts = Oferta.objects.filter(fecha_inicio__range = (today, timezone.now()))
    return render(request, 'oferts.html', {'oferts': oferts})

class Empleability(CreateView):
    model = Empleabilidad
    form_class = Empleabilidad_Form
    template_name = 'empleability.html'
    success_url = reverse_lazy("home")
    
def delete_candidato(request, id):
    aspirante = Aspirante.objects.get(id = id)
    if request.method == "POST":
        aspirante.delete()
        return redirect("/")
    return render(request, 'delete_candidate.html', {'aspirante': aspirante})

def delete_oferts(request, id):
    ofert = Oferta.objects.get(id = id)
    if request.method == "POST":
        ofert.delete()
        return redirect("/")
    return render(request, 'delete_ofert.html', {'ofert':ofert})

# def update_candidate(request, id):
#     aspirante = Aspirante.objects.get(id = id)
#     if request.method == 'GET':
#         form = Aspirante_Form(instance = aspirante)
#     else:
#         form = Aspirante_Form(request.POST, instance = aspirante)
#         if form.is_valid():
#             form.save()
#         return redirect("/")
#     return render(request,"register_candidate.html", {"form":form})

class Update_candidate(UpdateView):
    model = Aspirante
    form_class = Aspirante_Form
    template_name = 'register_candidate.html'
    success_url = reverse_lazy("home")

# def update_ofert(request, id):
#     oferta = Oferta.objects.get(id = id)
#     if request.method == 'GET':
#         form = Oferta_Form(instance = oferta)
#     else:
#         form = Oferta_Form(request.POST, instance = oferta)
#         if form.is_valid():
#             form.save()
#         return redirect("/")
#     return render(request,"ofert.html", {"form":form})

class Update_ofert(UpdateView):
    model = Oferta
    form_class = Oferta_Form
    template_name = 'ofert.html'
    success_url = reverse_lazy("home")

# def register_candidate(request):
#     form = Aspirante_Form()
#     if request.method == "POST":
#         form = Aspirante_Form(request.POST)#data= request.POST) = poder usar dato a dato
#         if form.is_valid():
#             form.save()
#             form = Aspirante_Form()
#             return redirect("/")
#                                         #optener dato a dato
#             # nombre = request.POST.get("nombre")
#             # edad = request.POST.get("edad")
#             # numero_cedula = request.POST.get("numero_cedula")
#             # id_profesion = request.POST.get("id_profesio")
#             # id_agencia = request.POST.get("id_agencia") 
#     return render(request, 'register_candidate.html', {'form': form})
# def ofert(request):
#     form = Oferta_Form()
#     if request.method == "POST":
#         form = Oferta_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             form = Oferta_Form()
#             return redirect("/")
#     return render(request, 'ofert.html', {'form': form})

# def empleability(request):
#     form = Empleabilidad_Form()
#     if request.method == "POST":
#         form = Empleabilidad_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             form = Empleabilidad_Form()
#             return redirect("/")
#     return render(request, "empleability.html", {'form': form})


def empleability(request):
    form = Empleabilidad_Form()
    if request.method == "POST":
        form = Empleabilidad_Form(data = request.POST)
        if form.is_valid():
            aspirante = int(request.POST.get("id_aspirante"))
            oferta = int(request.POST.get("id_oferta"))
            aspirantes = Empleabilidad.objects.filter(id_aspirante= aspirante)
            ofertas = Empleabilidad.objects.filter(id_oferta= oferta)
            lista = []
            lista1 = []
            if not aspirantes.exists() or not ofertas.exists():
                form.save()
                form = Empleabilidad_Form()
                return redirect("/")
            else:
                for aspiranteF in aspirantes:
                    for ofertaF in ofertas:
                        pass
                    if aspiranteF == ofertaF:
                        print("entra 3")
                        lista.append(aspiranteF)
                        lista1.append(ofertaF)
                        if lista == lista1:
                            return redirect("error")
                if ofertaF != aspiranteF:
                    print("entra 4")
                    form.save()
                    form = Empleabilidad_Form()
                    return redirect("/")
    return render(request, "empleability.html", {'form': form})

def error(request):
    return render(request, "error.html")