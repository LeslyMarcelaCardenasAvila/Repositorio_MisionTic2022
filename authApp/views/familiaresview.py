from ast import Delete
from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.familiares import Familiares
from authApp.serializers.familiaresserializer import Familiaresserializer

class CrearFamiliaresView(views.APIView):
    def post(self, request):
        serializar=Familiaresserializer(data=request.data)
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data,status=status.HTTP_201_CREATED)
        return Response(serializar.errors,status=status.HTTP_400_BAD_REQUEST)

class FamiliaresView(views.APIView):

    def get(self, request, pk, format=None):
        model= Familiares.objects.get(pk=pk)
        serializer= Familiaresserializer(model)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model= Familiares.objects.get(pk=pk)
        serializer= Familiaresserializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        modelo= Familiares.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)