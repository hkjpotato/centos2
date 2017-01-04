from django.db import models

class Feeder(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
        
    class Meta:
        db_table='Feeder'
