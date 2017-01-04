from django.db import models
from ..feeder_models import Feeder
from ..node_models import D_Bus

class D_Solar(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_solars')
    name = models.CharField(max_length=200)
    gld_index = models.IntegerField(null=True, default=0)
    
    generator_status = models.CharField(max_length=20, null=True)
    generator_mode = models.CharField(max_length=20, null=True)
    panel_type = models.CharField(max_length=50, null=True)
    efficiency = models.FloatField(null=True)
    #could be sf?
    area = models.CharField(max_length=30, null=True)
    orientation = models.CharField(max_length=30, null=True)
    orientation_azimuth = models.IntegerField(null=True)
    latitude_angle_fix = models.NullBooleanField(null=True)

    #for gld
    object = models.CharField(max_length=50, default='solar')

    #foreign key
    parent_bus = models.ForeignKey(D_Bus, related_name='solars')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_Solar'