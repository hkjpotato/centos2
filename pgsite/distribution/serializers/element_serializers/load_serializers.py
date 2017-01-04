from rest_framework import serializers
from distribution.models import \
D_Load

class DLoadSerializer(serializers.ModelSerializer):
    class Meta:
        # depth = 1
        model = D_Load
        fields = ('id', 'object', 'name', 'phases', 'nominal_voltage')
