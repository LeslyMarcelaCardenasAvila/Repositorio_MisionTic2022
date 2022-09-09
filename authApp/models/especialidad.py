from django.db import models
class Especialidad(models.Model):
    ID_especialidad=models.AutoField(primary_key=True)
    especialidad=models.CharField('especialidad',max_length=30)