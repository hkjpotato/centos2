from django.db import models

class D_LineSpacing(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    distance_AB = models.FloatField(default=0.0)
    distance_AC = models.FloatField(default=0.0)
    distance_AN = models.FloatField(default=0.0)
    distance_BC = models.FloatField(default=0.0)
    distance_BN = models.FloatField(default=0.0)
    distance_CN = models.FloatField(default=0.0)

    # for gld
    gld_index = models.IntegerField(null=True, default=0)
    object = models.CharField(max_length=50, default='line_spacing')
    
    def __unicode__(self):
        return self.name

    class Meta:
        db_table='D_LineSpacing'