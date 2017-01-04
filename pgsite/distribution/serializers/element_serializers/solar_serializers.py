from rest_framework import serializers
from distribution.models import \
D_Solar

class DSolarSerializer(serializers.ModelSerializer):
    class Meta:
        # depth = 1
        model = D_Solar
        fields = ('id', 'object', 'name', 'area', 'efficiency')
