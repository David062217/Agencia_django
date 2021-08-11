from django.contrib import admin
from .models import *
# Register your models here.

class ProfesionAdmin(admin.ModelAdmin):
    list_display = ('nombre')

admin.site.register(Profesion)
admin.site.register(Agencia)
admin.site.register(Oferta)
admin.site.register(Aspirante)
admin.site.register(Empleabilidad)