from django.db import models
from ..feeder_models import Feeder
from ..node_models import D_Bus
from ..elements import D_Meter


class D_Inverter(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_inverters')
    name = models.CharField(max_length=200)
    gld_index = models.IntegerField(null=True, default=0)


    #from gld
    phases = models.CharField(max_length=50, null=True)
    object = models.CharField(max_length=50, default='inverter')
    generator_mode = models.CharField(max_length=50, null=True)
    generator_status = models.CharField(max_length=50, null=True)
    inverter_type = models.CharField(max_length=50, null=True)
    power_factor = models.FloatField(null=True)
    inverter_efficiency = models.FloatField(null=True)

    #foreign key
    parent_bus = models.ForeignKey(D_Bus, related_name='inverters')
    parent_meter = models.ForeignKey(D_Meter, related_name='inverters')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_Inverter'