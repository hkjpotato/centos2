from rest_framework import serializers
from distribution.models import \
D_Generator

class DGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        # depth = 1
        model = D_Generator
        fields = ('id', 'object', 'name', 'capacity', 'cost')