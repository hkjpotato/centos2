from django.db import models
from ..feeder_models import Feeder
from ..node_models import D_Bus

class D_Load(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_loads')
    
    name = models.CharField(max_length=200)
    phases = models.CharField(max_length=50, null=True)
    #should be complex

    voltage_A = models.CharField(max_length=200, null=True)
    voltage_B = models.CharField(max_length=200, null=True)
    voltage_C = models.CharField(max_length=200, null=True)

    constant_power_A = models.CharField(max_length=200, null=True)
    constant_power_B = models.CharField(max_length=200, null=True)
    constant_power_C = models.CharField(max_length=200, null=True)

    nominal_voltage = models.FloatField(null=True)
    load_class = models.CharField(max_length=20, null=True)

    #for gld
    gld_index = models.IntegerField(null=True, default=0)
    object = models.CharField(max_length=50, default='load')

    #foreign key
    parent_bus = models.ForeignKey(D_Bus, related_name='loads')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_Load'