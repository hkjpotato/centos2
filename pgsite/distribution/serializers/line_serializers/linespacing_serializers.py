from rest_framework import serializers
from distribution.models import \
D_LineSpacing

class DLineSpacingSerializer(serializers.ModelSerializer):
    class Meta:
        # depth = 1
        model = D_LineSpacing
        fields = '__all__'