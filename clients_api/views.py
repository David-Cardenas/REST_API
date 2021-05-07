from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from clients_api import serializers

class HelloApiView(APIView):
  # Esta será la clase de una vista para pruebas
  serializer_class = serializers.HelloSerializer
  def get(self, request, format=None):
    # Retorna lista de caracteristicas del APIView 
    an_apiview = [
      'Usa metodos HTTP como funciones (get, post, patch, put, delete)',
      'Es similar a una vista que ofrece django usualmente',
      'Da un mayor control sobre la logica de la app',
      'Esta mapeado manualmente a los URL',         
    ]
    
    return Response({'message': 'Hello', 'an_apiview': an_apiview})
  
  def post(self, request):
    # Crea un mensaje con el nombre del cliente
    serializer = self.serializer_class(data=request.data)
    
    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello the product {name} was created successfully '
      return Response({'message' : message})
    else:
      return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
      )
    
  def put(self, request, pk=None):
    # Maneja la actualización de un objeto o producto en lista
    return Response({'method': 'PUT'})
  
  def patch(self, request, pk=None):
    # Maneja la actualizacion oarcial de un objeto
    return Response({'method': 'PATCH'})
  
  def delete(self, request, pk=None):
    # Maneja la eliminación de un objeto
    return Response({'method': 'DELETE'})
    

