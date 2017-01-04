from rest_framework import serializers
from distribution.models import \
D_Storage

class DStorageSerializer(serializers.ModelSerializer):
    class Meta:
        # depth = 1
        model = D_Storage
        fields = ('id', 'object', 'name', 'minCharge', 'maxCharge', 'chargeRate')
