from django.db import models
from ..feeder_models import Feeder
from ..node_models import D_Bus

class D_Switch(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_switches')
    name = models.CharField(max_length=100)
    phases = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    #foreign key
    from_bus = models.ForeignKey(D_Bus, related_name='from_switch', null=True)
    to_bus = models.ForeignKey(D_Bus, related_name='to_switch', null=True)

    # for gld
    gld_index = models.IntegerField(null=True, default=0)
    object = models.CharField(max_length=50, null=True, default='switch')

    class Meta:
        unique_together=('feeder', 'name') #each instance in a feeder has an unique name
        db_table='D_Switch'

    def __unicode__(self):
        return self.name