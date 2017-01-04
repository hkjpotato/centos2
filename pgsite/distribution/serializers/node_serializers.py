from rest_framework import serializers
# import feeder
# print 'xiaohaha'
# print feeder.__file__
# print dir()
from distribution.models import D_Bus

class DBusSerializer(serializers.ModelSerializer):
    # overheadlines
    class Meta:
        # depth = 1
        model = D_Bus
        fields = '__all__'