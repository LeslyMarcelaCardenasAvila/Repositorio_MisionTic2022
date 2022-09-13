from django.db import models
class Perfiles(models.Model):
    ID_Perfil=models.AutoField(primary_key=True)
    Perfil=models.CharField('perfil',max_length=30)