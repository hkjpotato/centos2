from django.db import models
from ..feeder_models import Feeder
from ..node_models import D_Bus
from ..elements import D_Meter, D_Inverter


class D_Battery(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_batterys')
    name = models.CharField(max_length=200)
    gld_index = models.IntegerField(null=True, default=0)

    #from gld
    generator_mode = models.CharField(max_length=50, null=True)
    V_Max = models.FloatField(null=True)
    I_Max = models.FloatField(null=True)
    P_Max = models.FloatField(null=True)
    E_Max = models.FloatField(null=True)
    base_efficiency = models.FloatField(null=True)
    parasitic_power_draw =  models.CharField(max_length=50, null=True)
    power_type =  models.CharField(max_length=50, null=True)
    generator_status =  models.CharField(max_length=50, null=True)
    Energy = models.FloatField(null=True)
    scheduled_power = models.CharField(max_length=50, null=True)
    power_factor = models.FloatField(null=True)

    object = models.CharField(max_length=50, default='battery')

    #foreign key
    parent_bus = models.ForeignKey(D_Bus, related_name='batterys')
    parent_inverter = models.ForeignKey(D_Inverter, related_name='batterys', null=True)
    parent_meter = models.ForeignKey(D_Meter, related_name='batterys', null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_Battery'