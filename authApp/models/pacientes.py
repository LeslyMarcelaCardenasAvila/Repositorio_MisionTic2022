from pyexpat import model
from django.db import models
from .familiares import Familiares
from .personalSalud import Personal_Salud

class Pacientes (models.Model):
    Cedula_Paciente=models.CharField(primary_key=True,unique=True,max_length=10)
    Cedula_Fliar=models.ForeignKey(Familiares,related_name='Pacientes',on_delete=models.CASCADE)
    cedulaPS=models.ForeignKey(Personal_Salud,related_name='Pacientes',on_delete=models.CASCADE)
    Nombres=models.CharField('nombre',max_length=30)
    Apellidos=models.CharField('apell',max_length=30)
    Fecha_Nac=models.DateField('fechanac',max_length=20)
    Genero=models.CharField('sexo',max_length=30)
    Celular=models.CharField('cel',max_length=10)
    Telefono=models.CharField('tel',max_length=10)
    Direccion=models.CharField('dire',max_length=10)
    Latitud=models.CharField('lat',max_length=20)
    Longitud=models.CharField('long',max_length=20)
    Ciudad=models.CharField('ciudad',max_length=20)
    Departamento=models.CharField('depar',max_length=20)
    Email=models.EmailField('email',max_length=100)

