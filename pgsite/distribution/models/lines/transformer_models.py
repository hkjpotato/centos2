from django.db import models
from ..feeder_models import Feeder
from ..node_models import D_Bus

class D_Transformer(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_transformers')
    name = models.CharField(max_length=100)
    phases = models.CharField(max_length=50)

    #foreign key
    from_bus = models.ForeignKey(D_Bus, related_name='from_transformer', null=True)
    to_bus = models.ForeignKey(D_Bus, related_name='to_transformer', null=True)
    configuration = models.ForeignKey('D_TransformerConfig', related_name='transformers', null=True, on_delete=models.SET_NULL)

    # for gld
    gld_index = models.IntegerField(null=True, default=0)
    groupid = models.CharField(max_length=50, default='Distribution_Trans')
    object = models.CharField(max_length=50, null=True, default='transformer')

    class Meta:
        unique_together=('feeder', 'name') #each instance in a feeder has an unique name
        db_table='D_Transformer'

    def __unicode__(self):
        return self.name

class D_TransformerConfig(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    connect_type = models.CharField(max_length=50, null=True)
    install_type = models.CharField(max_length=50, null=True)
    primary_voltage = models.FloatField(null=True)
    secondary_voltage = models.FloatField(null=True)
    power_rating = models.CharField(max_length=200, null=True)
    powerA_rating = models.FloatField(null=True)
    powerB_rating = models.FloatField(null=True)
    powerC_rating = models.FloatField(null=True)
    resistance = models.FloatField(null=True)
    reactance = models.FloatField(null=True)
    #could be complex
    impedance = models.CharField(max_length=50, null=True)
    shunt_impedance = models.CharField(max_length=50, null=True)

    # for gld
    gld_index = models.IntegerField(null=True, default=0)
    object = models.CharField(max_length=50, default='transformer_configuration')
    
    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_TransformerConfig'



