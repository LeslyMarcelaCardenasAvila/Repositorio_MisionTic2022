from rest_framework import serializers
from authApp.models.familiares import Familiares
class Familiaresserializer(serializers.ModelSerializer):
    class Meta:
        model=Familiares
        fields=('Cedula_Fliar','TipoID','Nombre','Apellido','Parentezco','Genero','Celular','Direccion','Municipio','Departamento','Email')