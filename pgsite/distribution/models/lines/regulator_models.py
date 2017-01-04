from django.db import models
from ..feeder_models import Feeder
from ..node_models import D_Bus

class D_Regulator(models.Model):
    id = models.AutoField(primary_key=True)
    feeder = models.ForeignKey(Feeder, related_name='d_regulators')
    name = models.CharField(max_length=100)
    phases = models.CharField(max_length=50)

    #foreign key
    from_bus = models.ForeignKey(D_Bus, related_name='from_regulator', null=True)
    to_bus = models.ForeignKey(D_Bus, related_name='to_regulator', null=True)
    configuration = models.ForeignKey('D_RegulatorConfig', related_name='regulators', null=True, on_delete=models.SET_NULL)
    senseNode =  models.ForeignKey(D_Bus, related_name='regulator', null=True)

    # for gld
    gld_index = models.IntegerField(null=True, default=0)
    object = models.CharField(max_length=50, null=True, default='regulator')

    class Meta:
        unique_together=('feeder', 'name') #each instance in a feeder has an unique name
        db_table='D_Regulator'

    def __unicode__(self):
        return self.name

class D_RegulatorConfig(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    connect_type = models.CharField(max_length=50, null=True)
    band_center = models.FloatField(null=True)
    band_width = models.FloatField(null=True)
    time_delay = models.FloatField(null=True)
    raise_taps = models.IntegerField(null=True)
    lower_taps = models.IntegerField(null=True)
    current_transducer_ratio = models.FloatField(null=True)
    power_transducer_ratio = models.FloatField(null=True)
    compensator_r_setting_A = models.FloatField(null=True)
    compensator_x_setting_A = models.FloatField(null=True)
    compensator_r_setting_B = models.FloatField(null=True)
    compensator_x_setting_B = models.FloatField(null=True)
    compensator_r_setting_C = models.FloatField(null=True)
    compensator_x_setting_C = models.FloatField(null=True)
    CT_phase = models.CharField(max_length=20, null=True)
    PT_phase = models.CharField(max_length=20, null=True)
    regulation = models.FloatField(null=True)
    Control = models.CharField(max_length=50, null=True)
    control_level = models.CharField(max_length=50, null=True)
    Type = models.CharField(max_length=50, null=True)
    tap_pos_A = models.IntegerField(null=True)
    tap_pos_B = models.IntegerField(null=True)
    tap_pos_C = models.IntegerField(null=True)


    # for gld
    gld_index = models.IntegerField(null=True, default=0)
    object = models.CharField(max_length=50, default='regulator_configuration')
    
    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_RegulatorConfig'



