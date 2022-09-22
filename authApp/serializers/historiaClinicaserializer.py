from rest_framework import serializers
from authApp.models.historiaClinica import historiaClinica
class historiaClinicaserializer(serializers.ModelSerializer):
    class Meta:
        model=historiaClinica
        fields=(' Cedula_Paciente','CedulaPS','Cedula_Fliar','Diagnostico','Examen_Fisico','Sugerencias','Evolucion')