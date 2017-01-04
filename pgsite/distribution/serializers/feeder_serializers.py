from rest_framework import serializers
# import feeder
# print 'xiaohaha'
# print feeder.__file__
# print dir()
from distribution.models import Feeder

class FeederSerializer(serializers.ModelSerializer):
    # overheadlines = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='overheadline-detail'
    # )

    # overheadlines
    class Meta:
        # depth = 1
        model = Feeder
        fields = '__all__'