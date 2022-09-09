from pyexpat import model
from django.db import models
from .especialidad import Especialidad
class Personal_Salud(models.Model):
    cedulaPS=models.CharField(primary_key=True,unique=True,max_length=10)
    ID_especialidad=models.ForeignKey(Especialidad,related_name='personaSalud',on_delete=models.CASCADE)
    Nombre=models.CharField('nombre',max_length=30)
    Apellido=models.CharField('apell',max_length=30)
    Genero=models.CharField('sexo',max_length=30)
    regMedico=models.CharField('registro',max_length=10)
    Celular=models.CharField('cel',max_length=10)
    Email=models.EmailField('email',max_length=100)