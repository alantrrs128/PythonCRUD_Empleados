from django.db import models
from django.utils import timezone

class Empleados(models.Model):
    PUESTOS = [
        ('RH', 'Recursos Humanos'),
        ('RI', 'Riesgos'),
        ('SE', 'Seguridad'),
        ('SI', 'Sistemas de Información'),
        ('TE', 'Tecnología'),
        ('DG', 'Digital'),
        ('DE', 'Director Ejecutivo'),
        ('DG', 'Director General'),
        ('DJ', 'Director Jurídico'),
        ('DT', 'Director Técnico'),
    ]
    nombre = models.CharField(max_length = 100, default = 'Nombre', null = False)
    apellidos = models.CharField(max_length = 50, default = '', null = False)
    puesto = models.CharField(max_length = 2, choices = PUESTOS, null = False)
    foto = models.FileField()
    creado = models.DateTimeField(auto_now_add = True)
    modificado = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'empleados'
