from rest_framework import serializers
from authApp.models.personalSalud import Personal_Salud
class Personal_saludserializer(serializers.ModelSerializer):
    class Meta:
        model=Personal_Salud
        fields=('cedulaPS','ID_especialidad','Nombre','Apellido','Genero','regMedico','Celular','Email')