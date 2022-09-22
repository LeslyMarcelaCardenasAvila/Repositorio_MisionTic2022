from rest_framework import serializers
from authApp.models.pacientes import Pacientes
class Pacientesserializer(serializers.ModelSerializer):
    class Meta:
        model=Pacientes
        fields=(' Cedula_Paciente','Cedula_Fliar','cedulaPS','Nombres','Apellidos','Fecha_Nac','Genero','Celular','Telefono','Direccion','Latitud','Longitud','Ciudad','Departamento','Email')