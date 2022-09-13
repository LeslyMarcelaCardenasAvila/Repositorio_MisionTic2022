from pyexpat import model
from tkinter import CASCADE
from django.db import models 
from .historiaClinica import historiaClinica
class Signosvitales(models.Model):
    ID_Signos=models.AutoField(primary_key=True)
    ID_HistC=models.ForeignKey(historiaClinica,related_name='signosvitales',on_delete=models.CASCADE)
    Fecha=models.DateField()
    Hora=models.TimeField()
    Fre_Cardiaca=models.IntegerField()
    Fre_Respiratoria=models.IntegerField()
    Pre_Arterial=models.IntegerField()
    Temperatura=models.IntegerField()
    Oximetria=models.IntegerField()
    Glicemia=models.IntegerField()