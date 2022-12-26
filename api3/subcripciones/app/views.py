from django.shortcuts import render
from .serializers import  ServicioSerializer, ClienteSerializer, SubscripcionSerializer
from .models import Cliente, Servicio, Subscripcion
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework import viewsets, generics

@api_view(['GET','POST'])
def Servicio_list(request):
    if request.method=='GET':
        Servicios=Servicio.objects.all()
        serializer=ServicioSerializer(Servicios,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def Servicio_crud(request,pk):
    try:
        Servicios=Servicio.objects.get(pk=pk)
    except Servicio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer= ServicioSerializer(Servicios)
        return Response(serializer.data)
    
    if request.method =='PUT':
        serializer=ServicioSerializer(Servicios,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        Servicios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])
def Cliente_list(request):
    if request.method=='GET':
        Clientes=Cliente.objects.all()
        serializer=ClienteSerializer(Clientes,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','DELETE'])
def Cliente_crud(request,pk):
    try:
        Clientes=Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer= ClienteSerializer(Clientes)
        return Response(serializer.data)

    if request.method =='PUT':
        serializer=ClienteSerializer(Clientes,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Clientes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])
def Subscripcion_list(request):
    if request.method=='GET':
        Subscripcions=Subscripcion.objects.all()
        serializer=SubscripcionSerializer(Subscripcions,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=SubscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','DELETE'])
def Subscripcion_crud(request,pk):
    try:
        Subscripcions=Subscripcion.objects.get(pk=pk)
    except Subscripcions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer= SubscripcionSerializer(Subscripcions)
        return Response(serializer.data)

    if request.method =='PUT':
        serializer=SubscripcionSerializer(Subscripcions,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Subscripcions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SubscripcionViewSet(viewsets.ModelViewSet):
    queryset = Subscripcion.objects.all()
    serializer_class = SubscripcionSerializer
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class ProfesorLista(generics.ListCreateAPIView):
    queryset=Cliente.objects.all()
    serializer_class=ClienteSerializer

class ProfesorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Cliente.objects.all()
    serializer_class=ClienteSerializer

class ProfesorLista(generics.ListCreateAPIView):
    queryset=Servicio.objects.all()
    serializer_class=ServicioSerializer

class ProfesorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Servicio.objects.all()
    serializer_class=ServicioSerializer
    
class ProfesorLista(generics.ListCreateAPIView):
    queryset=Subscripcion.objects.all()
    serializer_class=SubscripcionSerializer

class ProfesorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Subscripcion.objects.all()
    serializer_class=SubscripcionSerializer
