from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from authApp.models.usuario import Usuario
class Usuarioserializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=('ID_perfil','Username','Password')