from rest_framework import viewsets

#import model
from distribution.models import *
#import serializer
from distribution.serializers import *

class FeederViewSet(viewsets.ModelViewSet):
    queryset = Feeder.objects.all()
    serializer_class = FeederSerializer


class DBusViewSet(viewsets.ModelViewSet):
    queryset = D_Bus.objects.all()
    serializer_class = DBusSerializer

class DLoadViewSet(viewsets.ModelViewSet):
    queryset = D_Load.objects.all()
    serializer_class = DLoadSerializer

class DBatteryViewSet(viewsets.ModelViewSet):
    queryset = D_Battery.objects.all()
    serializer_class = DBatterySerializer


class DGeneratorViewSet(viewsets.ModelViewSet):
    queryset = D_Generator.objects.all()
    serializer_class = DGeneratorSerializer

class DCapacitorViewSet(viewsets.ModelViewSet):
    queryset = D_Capacitor.objects.all()
    serializer_class = DCapacitorSerializer

class DSolarViewSet(viewsets.ModelViewSet):
    queryset = D_Solar.objects.all()
    serializer_class = DSolarSerializer

class DStorageViewSet(viewsets.ModelViewSet):
    queryset = D_Storage.objects.all()
    serializer_class = DStorageSerializer

class DOverheadLineViewSet(viewsets.ModelViewSet):
    queryset = D_OverheadLine.objects.all()
    serializer_class = DOverheadLineSerializer

class DOverheadLineConfigViewSet(viewsets.ModelViewSet):
    queryset = D_OverheadLineConfig.objects.all()
    serializer_class = DOverheadLineConfigSerializer

class DOverheadLineConductorViewSet(viewsets.ModelViewSet):
    queryset = D_OverheadLineConductor.objects.all()
    serializer_class = DOverheadLineConductorSerializer


class DLineSpacingViewSet(viewsets.ModelViewSet):
    queryset = D_LineSpacing.objects.all()
    serializer_class = DLineSpacingSerializer