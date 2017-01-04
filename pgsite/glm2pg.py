import sys
import os
import json
import copy
from glmgen.feeder import GlmFile
glmFileObject = GlmFile.load("./data/IEEE13_Bus_DERModified_battery_Loads_PV.glm")

with open('./data/original_gen.json', 'w') as outFile:
    json.dump(glmFileObject, outFile, indent=4)

'''
flat the glmgen json structure
'''

from glmgen.feeder import fullyDeEmbed
fullyDeEmbed(glmFileObject)
'''
filter out the non-network related data
network related data:
networkdata = {
    "node": 1,
    "line_spacing": 1,
    "line_configuration": 1,

    "overhead_line": 1,
    "overhead_line_conductor": 1,

    "undeground_line": 1,
    "undeground_line_conductor": 1,

    "regulator": 1,
    "regulator_configuration": 1,

    "transformer": 1,
    "transformer_configuration": 1,

    "switch": 1,

    "load": 1,
    "capacitor": 1,
    "battery": 1,
    "meter": 1,
    "inverter": 1,
}
'''
networkdata = {
    "node": 1,
    "line_spacing": 1,
    "line_configuration": 1,

    "overhead_line": 1,
    "overhead_line_conductor": 1,

    "underground_line": 1,
    "underground_line_conductor": 1,

    "regulator": 1,
    "regulator_configuration": 1,

    "transformer": 1,
    "transformer_configuration": 1,

    "switch": 1,

    "load": 1,
    "capacitor": 1,
    "battery": 1,
    "meter": 1,
    "inverter": 1,
}

pgObject = {}
index = 0
for key in glmFileObject:
    currObj = glmFileObject[key]
    if 'object' in currObj and currObj['object'] in networkdata:
        pgObject[index] = currObj
        index += 1

# with open('pg.json', 'w') as outFile:
#     json.dump(pgObject, outFile, indent=4)
'''
modify them to database format
object battery1 {
    parent inverter1
}

object inverter1 {
    parent meter1
}

object meter1 {
    parent bus1
}
    ....

object battery {
    parentBus bus1
    parentMeter meter1
    parentInverter inverter1
}
'''

pgObject = GlmFile(pgObject)
#get the corresponding list
batteryList = pgObject.get_objects_by_type('battery')
inverterList = pgObject.get_objects_by_type('inverter')
meterList = pgObject.get_objects_by_type('meter')

# loop through the lowest level element and look for its parents
for b in batteryList:
    #get its own key
    selfKey = pgObject.get_object_key_by_name(b['name'])
    currEle = currBattery = pgObject[selfKey]
    #pointer
    p_Inverter = None
    p_Meter = None
    while ('parent' in currEle):
        #the current object has a parent
        parentName = currEle['parent']
        parentKey = pgObject.get_object_key_by_name(parentName)
        #the parent object
        parentEle = pgObject[parentKey]
        parentObject = parentEle['object']
        parentAttribute = 'parent_' + (parentObject if parentObject != 'node' else 'bus')
        #update battery
        currBattery[parentAttribute] = parentName
        #update inverter & meter if they exits
        if p_Inverter:
            p_Inverter[parentAttribute] = parentName
        if p_Meter:
            p_Meter[parentAttribute] = parentName

        if parentObject == 'inverter':
            p_Inverter = parentEle
        if parentObject == 'meter':
            p_Meter = parentEle
        #move to upper level
        del currEle['parent']
        currEle = parentEle

#other element should be fine, change parent to parent_bus directly
for key in pgObject:
    if 'parent' in pgObject[key]:
        parentName = pgObject[key]['parent']
        del pgObject[key]['parent']
        pgObject[key]['parent_bus'] = parentName

    #we dont need to store comment in databse
    if 'comment' in pgObject[key]:
        del pgObject[key]['comment']

for key in pgObject:
    pgObject[key]['gld_index'] = key

with open('./data/pg.json', 'w') as outFile:
    json.dump(pgObject, outFile, indent=4)