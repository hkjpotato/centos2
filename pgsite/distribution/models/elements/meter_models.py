from django.db import models
from ..feeder_models import Feeder
from ..node_models import D_Bus

class D_Meter(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_meters')
    name = models.CharField(max_length=200)
    gld_index = models.IntegerField(null=True, default=0)
    
    #from gld
    phases = models.CharField(max_length=50, null=True)
    voltage_A = models.CharField(max_length=200, null=True)
    voltage_B = models.CharField(max_length=200, null=True)
    voltage_C = models.CharField(max_length=200, null=True)
    nominal_voltage = models.FloatField(null=True)
    object = models.CharField(max_length=50, default='meter')

    #foreign key
    parent_bus = models.ForeignKey(D_Bus, related_name='meters')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_Meter'