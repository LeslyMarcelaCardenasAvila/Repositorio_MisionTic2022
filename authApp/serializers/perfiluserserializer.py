from rest_framework import serializers
from authApp.models.perfiluser import Perfiles
class Perfiluserserializer(serializers.ModelSerializer):
    class Meta:
        model=Perfiles
        fields=('Perfil')