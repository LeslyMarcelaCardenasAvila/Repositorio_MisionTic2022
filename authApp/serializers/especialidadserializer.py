from rest_framework import serializers
from authApp.models.especialidad import Especialidad
class Especialidadserializer(serializers.ModelSerializer):
    class Meta:
        model=Especialidad
        fields=('especialidad')