from pyexpat import model 
from django.db import models
from .pacientes import Pacientes   
from .personalSalud import Personal_Salud
from .familiares import Familiares

class historiaClinica (models.Model):
    Cedula_Paciente=models.ForeignKey(Pacientes,related_name='historiaClinica',on_delete=models.CASCADE)
    CedulaPS=models.ForeignKey(Personal_Salud,related_name='historiaClinica',on_delete=models.CASCADE)
    Cedula_Fliar=models.ForeignKey(Familiares,related_name='historiaClinica',on_delete=models.CASCADE)
    ID_HistC =models.AutoField(primary_key=True)
    Diagnostico=models.CharField('diagnos',max_length=200)
    Examen_Fisico=models.CharField('examen',max_length=200)
    Sugerencias=models.CharField('sug',max_length=200)
    Evolucion=models.CharField('evol',max_length=200)