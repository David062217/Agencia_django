from django.db import models
from django.db.models.base import ModelState

# Create your models here.

class Profesion(models.Model):
    profesion_choices = (
        ("Abogado", "Abogado"),
        ("I. Sistemas", "I. Sistemas"),
        ("A. Empresas", "A. Empresas"),
        ("Psicólogo", "Psicólogo"),
    )
    nombre = models.CharField(max_length = 20, choices = profesion_choices)
    
    class Meta:
        verbose_name = 'profesion'
        verbose_name_plural = 'profesiones'

    def __str__(self):
        return self.nombre

class Agencia(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=16)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Oferta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Aspirante(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    numero_cedula = models.CharField(max_length = 12, null=True)
    genero_choices = (
        ("f", "Femenino"),
        ("m", "Masculino"),
        ("o", "Otro"),
    )
    genero = models.CharField(max_length= 1, choices= genero_choices)
    id_profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    id_agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'aspirantes'
    
    def __str__(self):
        return self.nombre

class Empleabilidad(models.Model):
    id_aspirante = models.ForeignKey(Aspirante, on_delete=models.CASCADE)
    id_oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'empleabilidad'
