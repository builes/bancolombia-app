from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from guion.models import Dialogo, Escena, Guion, HistorialCambios
from .serializers import DialogoSerializer, EscenaSerializer, GuionSerializer, HistorialCambiosSerializer
from django.http import Http404



class DialogoListView(generics.ListCreateAPIView):
    queryset = Dialogo.objects.all()
    serializer_class = DialogoSerializer

class DialogoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dialogo.objects.all()
    serializer_class = DialogoSerializer




    
class EscenaListView(generics.ListCreateAPIView):
    queryset = Escena.objects.all()
    serializer_class = EscenaSerializer

class EscenaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Escena.objects.all()
    serializer_class = EscenaSerializer




class GuionList(generics.ListCreateAPIView):
    queryset = Guion.objects.all()
    serializer_class = GuionSerializer

class GuionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guion.objects.all()
    serializer_class = GuionSerializer





class HistorialCambiosList(generics.ListCreateAPIView):
    queryset = HistorialCambios.objects.all()
    serializer_class = HistorialCambiosSerializer

class HistorialCambiosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistorialCambios.objects.all()
    serializer_class = HistorialCambiosSerializer