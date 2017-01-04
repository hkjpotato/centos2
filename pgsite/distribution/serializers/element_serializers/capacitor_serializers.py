from rest_framework import serializers
from distribution.models import \
D_Capacitor

class DCapacitorSerializer(serializers.ModelSerializer):
    class Meta:
        # depth = 1
        model = D_Capacitor
        fields = '__all__'