from django.db import models
from .feeder_models import Feeder

class D_Bus(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_buses')
    name = models.CharField(max_length=200)
    phases = models.CharField(max_length=50, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    bustype = models.CharField(max_length=20, null = True)

    #should be complex
    voltage_A = models.CharField(max_length=200, null=True)
    voltage_B = models.CharField(max_length=200, null=True)
    voltage_C = models.CharField(max_length=200, null=True)
    nominal_voltage = models.FloatField(null=True)
    
    #for gld
    gld_index = models.IntegerField(null=True, default=0)
    object = models.CharField(max_length=50, default='node')

    #foreign key
    parent_bus = models.ForeignKey("D_Bus", related_name='child_bus', null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_Bus'
