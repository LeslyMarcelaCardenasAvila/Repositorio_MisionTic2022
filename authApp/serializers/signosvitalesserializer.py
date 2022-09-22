from rest_framework import serializers
from authApp.models.signosvitales import Signosvitales
class Signosvitalesserializer(serializers.ModelSerializer):
    class Meta:
        model=Signosvitales
        fields=(' ID_HistC','Fecha','Hora','Fre_Cardiaca','Fre_Respiratoria','Pre_Arterial','Temperatura','Oximetria','Glicemia')