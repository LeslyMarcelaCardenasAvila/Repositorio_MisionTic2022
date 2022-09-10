from pyexpat import model
from tkinter import CASCADE
from django.db import models 
from .historiaClinica import historiaClinica
class Signosvitales(models.Model):
    ID_Signos=models.AutoField(primary_key=True,unique=True,max_length=10)
    ID_HistC=models.ForeignKey(historiaClinica,related_name='signosvitales',on_delete=models.CASCADE)
    Fecha=models.DateField('fecha',max_length=20)
    Hora=models.TimeField('hora',max_length=20)
    Fre_Cardiaca=models.IntegerField('frecard',max_length=10)
    Fre_Respiratoria=models.IntegerField('freresp',max_length=10)
    Pre_Arterial=models.IntegerField('preart',max_length=10)
    Temperatura=models.IntegerField('temp',max_length=10)
    Oximetria=models.IntegerField('Oxim',max_length=10)
    Glicemia=models.IntegerField('Glicem',max_length=10)