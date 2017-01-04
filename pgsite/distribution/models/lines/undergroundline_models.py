from django.db import models
from ..feeder_models import Feeder
from ..node_models import D_Bus
from .linespacing_models import D_LineSpacing

class D_UndergroundLine(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_undergroundlines')
    name = models.CharField(max_length=100)
    phases = models.CharField(max_length=50)
    length = models.FloatField(default=0)
    bmat = models.FloatField(null=True)

    #foreign key
    from_bus = models.ForeignKey(D_Bus, related_name='from_undergroundline', null=True)
    to_bus = models.ForeignKey(D_Bus, related_name='to_undergroundline', null=True)
    configuration = models.ForeignKey('D_UndergroundLineConfig', related_name='undergroundlines', null=True, on_delete=models.SET_NULL)
    
    # for gld
    gld_index = models.IntegerField(null=True, default=0)
    groupid = models.CharField(max_length=50, default='Distribution_Line')
    object = models.CharField(max_length=50, null=True, default='undergound_line')

    class Meta:
        unique_together=('feeder', 'name') #each instance in a feeder has an unique name
        db_table='D_UndergroundLine'

    def __unicode__(self):
        return self.name

class D_UndergroundLineConfig(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    #foreign key
    conductor_A = models.ForeignKey('D_UndergroundLineConductor', related_name='as_conductor_A', null=True, on_delete=models.SET_NULL)
    conductor_B = models.ForeignKey('D_UndergroundLineConductor', related_name='as_conductor_B', null=True, on_delete=models.SET_NULL)
    conductor_C = models.ForeignKey('D_UndergroundLineConductor', related_name='as_conductor_C', null=True, on_delete=models.SET_NULL)
    conductor_N = models.ForeignKey('D_UndergroundLineConductor', related_name='as_conductor_N', null=True, on_delete=models.SET_NULL)
    spacing = models.ForeignKey('D_LineSpacing', null=True, on_delete=models.SET_NULL)
    
    # for gld
    gld_index = models.IntegerField(null=True, default=0)
    object = models.CharField(max_length=50, default='line_configuration')
    
    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_UndergroundLineConfig'

class D_UndergroundLineConductor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    conductor_resistance = models.FloatField(null=True)
    shield_resistance = models.FloatField(null=True)
    neutral_gmr = models.FloatField(null=True)
    outer_diameter = models.FloatField(null=True)
    neutral_strands = models.FloatField(null=True)
    neutral_resistance = models.FloatField(null=True)
    neutral_diameter = models.FloatField(null=True)
    conductor_diameter = models.FloatField(null=True)
    shield_gmr = models.FloatField(null=True)
    conductor_gmr = models.FloatField(null=True)
    
    # for gld
    gld_index = models.IntegerField(null=True, default=0)
    object = models.CharField(max_length=50, default='underground_line_conductor')
    
    class Meta:
        db_table='D_UndergroundLineConductor'


