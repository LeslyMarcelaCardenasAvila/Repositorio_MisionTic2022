from ast import Delete
from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.signosvitales import Signosvitales
from authApp.serializers.signosvitalesserializer import Signosvitalesserializer

class CrearSignosVitalesView(views.APIView):
    def post(self, request):
        serializar=Signosvitales(data=request.data)
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data,status=status.HTTP_201_CREATED)
        return Response(serializar.errors,status=status.HTTP_400_BAD_REQUEST)

class SignosVitalesView(views.APIView):

    def get(self, request, pk, format=None):
        model= Signosvitales.objects.get(pk=pk)
        serializer=Signosvitalesserializer(model)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model= Signosvitales.objects.get(pk=pk)
        serializer= Signosvitalesserializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        modelo= Signosvitales.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)