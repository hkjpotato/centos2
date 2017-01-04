'''read a pgjson file into the current database'''
import os
import django
import json
import copy
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pgsite.settings")
django.setup()
from distribution.models import Feeder, D_Bus, D_Load, D_Capacitor
from distribution.models import D_Generator, D_Storage, D_Solar
from distribution.models import D_Meter, D_Inverter, D_Battery
from distribution.models import D_OverheadLine, D_UndergroundLine, D_Regulator, D_Transformer, D_Switch
from distribution.models import D_LineSpacing
from distribution.models import D_OverheadLineConfig, D_OverheadLineConductor
from distribution.models import D_UndergroundLineConfig, D_UndergroundLineConductor
from distribution.models import D_TransformerConfig, D_RegulatorConfig

with open('./data/pg.json', 'r') as infile:
    pgObject = json.load(infile)

#hard-code feedername
feederName = "IEEE13"

if Feeder.objects.filter(name = feederName).count() > 0:
    feeder = Feeder.objects.get(name = feederName)
    print 'Get from db'
else:
    feeder = Feeder.objects.create(name=feederName)
    print 'Create new Feeder', feederName

def makeD_Bus(key, busObject):
    busname = busObject['name']
    if feeder.d_buses.all().filter(name=busname).count() == 0:
        print 'create bus'
        #delete parent_bus attribute
        if 'parent_bus' in busObject:
            del busObject['parent_bus']
        #attach the data from json file
        bus = D_Bus(**busObject)
        #additional data for none database design
        bus.feeder = feeder
        bus.save()
    else:
        print 'already in db'

def getItemsByObject(pgObject, objectType):
    items = []
    for key in pgObject:
        currObject = copy.deepcopy(pgObject[key])
        if 'object' in currObject and currObject['object'] == objectType:
            items.append(currObject)
    # print items
    return items

# # Get bus info
print '------------read bus-------------'
print '---makedb bus----'
#bus without parent bus
for key in pgObject:
    currObject = copy.deepcopy(pgObject[key])
    if 'object' in currObject and currObject['object'] == 'node':
        makeD_Bus(key, currObject)
#attach parent bus if needed
for key in pgObject:
    currObject = copy.deepcopy(pgObject[key])
    if 'object' in currObject and currObject['object'] == 'node':
        if 'parent_bus' in currObject:
            currbus = feeder.d_buses.get(name=currObject['name'])
            currbus.parent_bus = feeder.d_buses.get(name=currObject['parent_bus'])
            currbus.save()

loadList = getItemsByObject(pgObject, 'load')
for loadData in loadList:
    loadName = loadData['name']
    if feeder.d_loads.filter(name=loadName).count() == 0:
        print 'create load'
        parent_bus = loadData['parent_bus']
        loadData['parent_bus'] = feeder.d_buses.get(name=parent_bus)
        instance = D_Load(**loadData)
        instance.feeder = feeder
        instance.save()  
    else:
        print 'already in db'

capacitorList = getItemsByObject(pgObject, 'capacitor')
for capacitorData in capacitorList:
    capacitorName = capacitorData['name']
    if feeder.d_capacitors.filter(name=capacitorName).count() == 0:
        print 'create capacitor'
        parent_bus = capacitorData['parent_bus']
        capacitorData['parent_bus'] = feeder.d_buses.get(name=parent_bus)
        instance = D_Capacitor(**capacitorData)
        instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'

meterList = getItemsByObject(pgObject, 'meter')
for meterData in meterList:
    meterName = meterData['name']
    if feeder.d_meters.filter(name=meterName).count() == 0:
        print 'create meter'
        parent_bus = meterData['parent_bus']
        meterData['parent_bus'] = feeder.d_buses.get(name=parent_bus)
        instance = D_Meter(**meterData)
        instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'

inverterList = getItemsByObject(pgObject, 'inverter')
for inverterData in inverterList:
    inverterName = inverterData['name']
    if feeder.d_inverters.filter(name=inverterName).count() == 0:
        print 'create inverter'
        if 'parent_bus' in inverterData:
            parent_bus = inverterData['parent_bus']
            inverterData['parent_bus'] = feeder.d_buses.get(name=parent_bus)
        if 'parent_meter' in inverterData:
            parent_meter = inverterData['parent_meter']
            inverterData['parent_meter'] = feeder.d_meters.get(name=parent_meter)
        instance = D_Inverter(**inverterData)
        instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'

# print getattr(feeder, 'd_buses')

batteryList = getItemsByObject(pgObject, 'battery')
for itemData in batteryList:
    itemName = itemData['name']
    if feeder.d_batterys.filter(name=itemName).count() == 0:
        print 'create item'
        if 'parent_bus' in itemData:
            parent_bus = itemData['parent_bus']
            itemData['parent_bus'] = feeder.d_buses.get(name=parent_bus)
        if 'parent_meter' in itemData:
            parent_meter = itemData['parent_meter']
            itemData['parent_meter'] = feeder.d_meters.get(name=parent_meter)
        if 'parent_inverter' in itemData:
            parent_inverter = itemData['parent_inverter']
            itemData['parent_inverter'] = feeder.d_inverters.get(name=parent_inverter)
        instance = D_Battery(**itemData)
        instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'


lsList = getItemsByObject(pgObject, 'line_spacing')
for itemData in lsList:
    itemName = itemData['name']
    if D_LineSpacing.objects.filter(name=itemName).count() == 0:
        print 'create linespacing'
        instance = D_LineSpacing(**itemData)
        # instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'

#create ohl-conductor
ohl_conductorList = getItemsByObject(pgObject, 'overhead_line_conductor')
for itemData in ohl_conductorList:
    itemName = itemData['name']
    if D_OverheadLineConductor.objects.filter(name=itemName).count() == 0:
        print 'create ohl_conductor'
        instance = D_OverheadLineConductor(**itemData)
        # instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'

#create ugl-conductor
ugl_conductorList = getItemsByObject(pgObject, 'underground_line_conductor')
for itemData in ugl_conductorList:
    itemName = itemData['name']
    if D_UndergroundLineConductor.objects.filter(name=itemName).count() == 0:
        print 'create ugl_conductor'
        instance = D_UndergroundLineConductor(**itemData)
        # instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'

def getConductorTypeByName(conductorName):
    #in glm file, it is assumed that each conductor should have a unique name
    for itemData in ohl_conductorList:
        if itemData['name'] == conductorName:
            return 'D_OverheadLineConductor'
    for itemData in ugl_conductorList:
        if itemData['name'] == conductorName:
            return 'D_UndergroundLineConductor'

#helper function to get the lineconfig type
def getLineConfigType(itemData):
    if 'conductor_A' in itemData:
        if getConductorTypeByName(itemData['conductor_A']) is 'D_OverheadLineConductor':
            return 'OverheadLineConfig'
        else:
            return 'UndergroundLineConfig'
    elif 'conductor_B' in itemData:
        if getConductorTypeByName(itemData['conductor_B']) is 'D_OverheadLineConductor':
            return 'OverheadLineConfig'
        else:
            return 'UndergroundLineConfig'
    elif 'conductor_C' in itemData:
        if getConductorTypeByName(itemData['conductor_C']) is 'D_OverheadLineConductor':
            return 'OverheadLineConfig'
        else:
            return 'UndergroundLineConfig'
    elif 'confuctor_N' in itemData:
        if getConductorTypeByName(itemData['conductor_N']) is 'D_OverheadLineConductor':
            return 'OverheadLineConfig'
        else:
            return 'UndergroundLineConfig'

#update the foreign key of line config
def updateOverheadLineConfigData(itemData):
    if 'conductor_A' in itemData:
        itemData['conductor_A'] = D_OverheadLineConductor.objects.get(name=itemData['conductor_A'])
    if 'conductor_B' in itemData:
        itemData['conductor_B'] = D_OverheadLineConductor.objects.get(name=itemData['conductor_B'])
    if 'conductor_C' in itemData:
        itemData['conductor_C'] = D_OverheadLineConductor.objects.get(name=itemData['conductor_C'])
    if 'conductor_N' in itemData:
        itemData['conductor_N'] = D_OverheadLineConductor.objects.get(name=itemData['conductor_N'])
    if 'spacing' in itemData:
        itemData['spacing'] = D_LineSpacing.objects.get(name=itemData['spacing'])

#update the foreign key of line config
def updateUndergroundLineConfigData(itemData):
    if 'conductor_A' in itemData:
        itemData['conductor_A'] = D_UndergroundLineConductor.objects.get(name=itemData['conductor_A'])
    if 'conductor_B' in itemData:
        itemData['conductor_B'] = D_UndergroundLineConductor.objects.get(name=itemData['conductor_B'])
    if 'conductor_C' in itemData:
        itemData['conductor_C'] = D_UndergroundLineConductor.objects.get(name=itemData['conductor_C'])
    if 'conductor_N' in itemData:
        itemData['conductor_N'] = D_UndergroundLineConductor.objects.get(name=itemData['conductor_N'])
    if 'spacing' in itemData:
        itemData['spacing'] = D_LineSpacing.objects.get(name=itemData['spacing'])


lineConfig_list = getItemsByObject(pgObject, 'line_configuration')
for itemData in lineConfig_list:
    if getLineConfigType(itemData) is 'OverheadLineConfig':
        if D_OverheadLineConfig.objects.filter(name=itemData['name']).count() == 0:
            print 'create overheadline_config'
            updateOverheadLineConfigData(itemData)
            instance = D_OverheadLineConfig(**itemData)
            # instance.feeder = feeder
            instance.save()
        else:
            print 'already in db'
    elif getLineConfigType(itemData) is 'UndergroundLineConfig':
        if D_UndergroundLineConfig.objects.filter(name=itemData['name']).count() == 0:
            print 'create undergroundline_config'
            updateUndergroundLineConfigData(itemData)
            instance = D_UndergroundLineConfig(**itemData)
            # instance.feeder = feeder
            instance.save()
        else:
            print 'already in db'
    else:
        print 'it is impossible to have other line config'


def updateUndergroundLineConfigData(itemData):
    if 'conductor_A' in itemData:
        itemData['conductor_A'] = D_UndergroundLineConductor.objects.get(name=itemData['conductor_A'])
    if 'conductor_B' in itemData:
        itemData['conductor_B'] = D_UndergroundLineConductor.objects.get(name=itemData['conductor_B'])
    if 'conductor_C' in itemData:
        itemData['conductor_C'] = D_UndergroundLineConductor.objects.get(name=itemData['conductor_C'])
    if 'conductor_N' in itemData:
        itemData['conductor_N'] = D_UndergroundLineConductor.objects.get(name=itemData['conductor_N'])
    if 'spacing' in itemData:
        itemData['spacing'] = D_LineSpacing.objects.get(name=itemData['spacing'])


ohl_list = getItemsByObject(pgObject, 'overhead_line')
for itemData in ohl_list:
    if D_OverheadLine.objects.filter(name=itemData['name']).count() == 0:
        print 'create overheadline'
        if 'configuration' in itemData:
            itemData['configuration'] = D_OverheadLineConfig.objects.get(name=itemData['configuration'])
        if 'from' in itemData:
            itemData['from_bus'] = feeder.d_buses.get(name=itemData['from'])
            del itemData['from']
        if 'to' in itemData:
            itemData['to_bus'] = feeder.d_buses.get(name=itemData['to'])
            del itemData['to']
        instance = D_OverheadLine(**itemData)
        instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'

ugl_list = getItemsByObject(pgObject, 'underground_line')
for itemData in ugl_list:
    if D_UndergroundLine.objects.filter(name=itemData['name']).count() == 0:
        print 'create undergroundline'
        if 'configuration' in itemData:
            itemData['configuration'] = D_UndergroundLineConfig.objects.get(name=itemData['configuration'])
        if 'from' in itemData:
            itemData['from_bus'] = feeder.d_buses.get(name=itemData['from'])
            del itemData['from']
        if 'to' in itemData:
            itemData['to_bus'] = feeder.d_buses.get(name=itemData['to'])
            del itemData['to']
        instance = D_UndergroundLine(**itemData)
        instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'


'''
other link: switch, transoformer and 
'''

#read switch element
switch_list = getItemsByObject(pgObject, 'switch')
for itemData in switch_list:
    if D_Switch.objects.filter(name=itemData['name']).count() == 0:
        print 'create switch'
        if 'from' in itemData:
            itemData['from_bus'] = feeder.d_buses.get(name=itemData['from'])
            del itemData['from']
        if 'to' in itemData:
            itemData['to_bus'] = feeder.d_buses.get(name=itemData['to'])
            del itemData['to']
        instance = D_Switch(**itemData)
        instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'

#read transformer config
t_config_list = getItemsByObject(pgObject, 'transformer_configuration')
for itemData in t_config_list:
    if D_TransformerConfig.objects.filter(name=itemData['name']).count() == 0:
        print 'create trans_config'
        instance = D_TransformerConfig(**itemData)
        # instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'

#read transformer 
transformer_list = getItemsByObject(pgObject, 'transformer')
for itemData in transformer_list:
    if D_Transformer.objects.filter(name=itemData['name']).count() == 0:
        print 'create transformer'
        if 'configuration' in itemData:
            itemData['configuration'] = D_TransformerConfig.objects.get(name=itemData['configuration'])
        if 'from' in itemData:
            itemData['from_bus'] = feeder.d_buses.get(name=itemData['from'])
            del itemData['from']
        if 'to' in itemData:
            itemData['to_bus'] = feeder.d_buses.get(name=itemData['to'])
            del itemData['to']
        instance = D_Transformer(**itemData)
        instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'

#read regulator config
r_config_list = getItemsByObject(pgObject, 'regulator_configuration')
for itemData in r_config_list:
    if D_RegulatorConfig.objects.filter(name=itemData['name']).count() == 0:
        print 'create trans_config'
        instance = D_RegulatorConfig(**itemData)
        # instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'

#read regulator 
regulator_list = getItemsByObject(pgObject, 'regulator')
for itemData in regulator_list:
    if D_Regulator.objects.filter(name=itemData['name']).count() == 0:
        print 'create regulator'
        if 'configuration' in itemData:
            itemData['configuration'] = D_RegulatorConfig.objects.get(name=itemData['configuration'])
        if 'from' in itemData:
            itemData['from_bus'] = feeder.d_buses.get(name=itemData['from'])
            del itemData['from']
        if 'to' in itemData:
            itemData['to_bus'] = feeder.d_buses.get(name=itemData['to'])
            del itemData['to']
        instance = D_Regulator(**itemData)
        instance.feeder = feeder
        instance.save()
    else:
        print 'already in db'