from rest_framework import serializers
from guion.models import Guion, Escena, Dialogo, HistorialCambios

class DialogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialogo
        fields = '__all__'

class EscenaSerializer(serializers.ModelSerializer):
    dialogos = DialogoSerializer(many=True, read_only=True)

    class Meta:
        model = Escena
        fields = '__all__'

class GuionSerializer(serializers.ModelSerializer):
    escenas = EscenaSerializer(many=True, read_only=True)
    historial_cambios = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Guion
        fields = '__all__'

class HistorialCambiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialCambios
        fields = '__all__'
