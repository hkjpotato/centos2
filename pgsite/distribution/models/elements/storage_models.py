from django.db import models
from ..feeder_models import Feeder
from ..node_models import D_Bus

class D_Storage(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_storages')
    name = models.CharField(max_length=200)
    gld_index = models.IntegerField(null=True, default=0)
    
    minCharge = models.FloatField(null=True)
    maxCharge = models.FloatField(null=True)
    initialCharge = models.FloatField(null=True)
    chargeRate = models.FloatField(null=True)
    dischargeRate = models.FloatField(null=True)
    chargeEff = models.FloatField(null=True)
    dischargeEff = models.FloatField(null=True)
    #for gld
    object = models.CharField(max_length=50, default='storage')
    #foreign key
    parent_bus = models.ForeignKey(D_Bus, related_name='storages')


    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_Storage'