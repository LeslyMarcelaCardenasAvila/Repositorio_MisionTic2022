from django.db import models
from .perfiluser import Perfiles
class Usuario(models.Model):
    ID_usuario=models.AutoField(primary_key=True)
    ID_perfil=models.ForeignKey(Perfiles,related_name='usuario',on_delete=models.CASCADE)
    Username=models.CharField('username',max_length=30)
    Password=models.CharField('passw',max_length=30)