from ast import Delete
from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from authApp.models.usuario import Usuario
from authApp.serializers.usuarioserializer import Usuarioserializer

class CrearUsuarioView(views.APIView):
    def post(self, request):
        serializar=Usuarioserializer(data=request.data)
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data,status=status.HTTP_201_CREATED)
        return Response(serializar.errors,status=status.HTTP_400_BAD_REQUEST)

class UsuarioView(views.APIView):

    def get(self, request, pk, format=None):
        model= Usuario.objects.get(pk=pk)
        serializer=Usuarioserializer(model)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        model= Usuario.objects.get(pk=pk)
        serializer= Usuarioserializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        modelo= Usuario.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
