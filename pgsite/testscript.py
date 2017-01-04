'''
set up the django environment so that it can connect to the right database
'''
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pgsite.settings")
django.setup()

'''
import the models that you want to use
'''
from distribution.models import Feeder, D_Bus, D_Load, D_Capacitor
from distribution.models import D_Generator, D_Storage, D_Solar
from distribution.models import D_OverheadLine, D_UndergroundLine, D_Regulator, D_Transformer, D_Switch
from distribution.models import D_LineSpacing
from distribution.models import D_OverheadLineConfig, D_OverheadLineConductor
from distribution.models import D_UndergroundLineConfig, D_UndergroundLineConductor
from distribution.models import D_TransformerConfig, D_RegulatorConfig

'''
source document: making query in django ORM https://docs.djangoproject.com/en/1.10/topics/db/queries/
'''

#get the feeder instance that you want to use by name
myFeeder = Feeder.objects.get(name='IEEE13')
print myFeeder

'''
get all the bus instances belong to this feeder, two options
'''
#option1, filter by feeder
print '........'
myBusList1 = D_Bus.objects.filter(feeder=myFeeder)
for bus in myBusList1:
    print bus.name, bus.nominal_voltage

#option2, use feeder to 
print '........'
myBusList2 = myFeeder.d_buses.all()
for bus in myBusList2:
    print bus.name, bus.nominal_voltage


'''
get the bus as a native python dict
'''
myBus1 = myFeeder.d_buses.all()[0] #this is an instance
print type(myBus1), myBus1
myBus1Value = myFeeder.d_buses.all().values()[0]
print type(myBus1Value), myBus1Value


'''
write raw sql without ORM
https://docs.djangoproject.com/en/1.9/topics/db/sql/
'''
print 'use raw sql'
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT * FROM D_Bus")
row = cursor.fetchone()
print row