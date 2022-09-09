from pyexpat import model
from django.db import models
class Familiares(models.Model):
    Cedula_Fliar=models.CharField(primary_key=True,unique=True,max_length=10)
    TipoID=models.CharField('tipo',max_length=10)
    Nombre=models.CharField('nombre',max_length=30)
    Apellido=models.CharField('apell',max_length=30)
    Parentezco=models.CharField('flia',max_length=30)
    Genero=models.CharField('sexo',max_length=30)
    Celular=models.CharField('cel',max_length=10)
    Direccion=models.CharField('dir',max_length=30)
    Municipio=models.CharField('muni',max_length=30)
    Departamento=models.CharField('dpto',max_length=30)
    Email=models.EmailField('email',max_length=100)