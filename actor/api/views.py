
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from actor.models import Actor, Pose, Ubicacion
from .serializers import ActorSerializer, PoseSerializer, UbicacionSerializer
from django.http import Http404


class ActorListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer



class PoseListView(generics.ListCreateAPIView):
    queryset = Pose.objects.all()
    serializer_class = PoseSerializer

class PoseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pose.objects.all()
    serializer_class = PoseSerializer



class UbicacionListView(generics.ListCreateAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class UbicacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer