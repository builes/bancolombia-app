from rest_framework import serializers
from actor.models import Actor, Pose, Ubicacion

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class PoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pose
        fields = '__all__'

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'
