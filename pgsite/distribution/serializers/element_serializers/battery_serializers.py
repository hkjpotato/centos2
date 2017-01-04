from rest_framework import serializers
from distribution.models import \
D_Battery

class DBatterySerializer(serializers.ModelSerializer):
    class Meta:
        # depth = 1
        model = D_Battery
        fields = '__all__'