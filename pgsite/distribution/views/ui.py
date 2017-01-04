from django.shortcuts import render, render_to_response
from distribution.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json

templatePrefix = 'distribution'

# Create your views here.
def test(request):
    return HttpResponse('hello')

def testui(request):
    return render_to_response(templatePrefix + '/' + 'testui.html', locals())

# def feederDataTest(request):
#     if 'zoomLevel' in request.GET:
#         zoomLevel = request.GET['zoomLevel']
#         print 'zoomLevel', zoomLevel
#     zoomLevel = int(request.GET.get('zoomLevel', 12))
#     pgObj = {}
#     if (zoomLevel <= 13):
#         print 'smaller than 13'
#         with open("data/" + "nyc_transmission.json", "r") as transmission:
#             transdata = json.load(transmission)
#         pgObj.update(transdata)
#     else:
#         print 'larger than 13'
#         # feederData = makeFeeder("Circuit01")
#         # pgObj.update(feederData)
#         # print 'we really try'
#         with open("data/" + "all.json", "r") as all:
#             transdata = json.load(all)
#         pgObj.update(transdata)
#         # with open("data/" + "all" + ".json", "w") as outFile:
#             # json.dump(pgObj, outFile, indent=4)
#     data = pgObj
#     return JsonResponse(data, safe=False)


def feederDataTest(request):
    pgObj = {}
    feederData = makeFeeder("IEEE13")
    pgObj.update(feederData)
    data = pgObj
    return JsonResponse(data, safe=False)

def makeFeeder(feederName):
    # step 1: fetch data from SQL
    feederName = feederName
    feeder = Feeder.objects.get(name = feederName)
    d_bus = feeder.d_buses.select_related().all()
    d_capacitor = feeder.d_capacitors.select_related().all()
    d_generator = feeder.d_generators.select_related().all()
    d_storage = feeder.d_storages.select_related().all()
    d_solar = feeder.d_solars.select_related().all()
    d_load = feeder.d_loads.select_related().all()
    d_overheadline = feeder.d_overheadlines.select_related().all()
    d_transformer = feeder.d_transformers.select_related().all()
    d_undergroundline = feeder.d_undergroundlines.select_related().all()
    d_switch = feeder.d_switches.select_related().all()
    d_regulator = feeder.d_regulators.select_related().all()

    d_battery = feeder.d_batterys.select_related().all()
    # d_meter = feeder.d_meters.select_related().all()
    # d_inverter = feeder.d_inverters.select_related().all()



    #step 2: construct the tree object used by omf
    pgObj = {}
    # gldIndex = 0
    # print [f.name for f in D_BUS._meta.get_fields()]
    for node in d_bus:
        pgObj[node.gld_index] = {
            "id": node.id,
            "gldIndex": node.gld_index,
            "name": node.name,
            "object": node.object,
            # "lng": float(node.lng),
            # "lat": float(node.lat)
        }
        if node.parent_bus:
            pgObj[node.gld_index]['parent'] = node.parent_bus.name
    for node in d_capacitor:
        pgObj[node.gld_index] = {
            "id": node.id,
            "gldIndex": node.gld_index,
            "name": node.name,
            "object": node.object,
            "parent": node.parent_bus.name,
        }
    for node in d_generator:
        pgObj[node.gld_index] = {
            "id": node.id,
            "gldIndex": node.gld_index,
            "name": node.name,
            "object": node.object,
            "parent": node.parent_bus.name,
        }


    for node in d_storage:
        pgObj[node.gld_index] = {
            "id": node.id,
            "gldIndex": node.gld_index,
            "name": node.name,
            "object": node.object,
            "parent": node.parent_bus.name,
        }

    for node in d_solar:
        pgObj[node.gld_index] = {
            "id": node.id,
            "gldIndex": node.gld_index,
            "name": node.name,
            "object": node.object,
            "parent": node.parent_bus.name,

        }

    for node in d_battery:
        pgObj[node.gld_index] = {
            "id": node.id,
            "gldIndex": node.gld_index,
            "name": node.name,
            "object": node.object,
            "parent": node.parent_bus.name,
        }

    for node in d_load:
        pgObj[node.gld_index] = {
            "id": node.id,
            "gldIndex": node.gld_index,
            "name": node.name,
            "object": node.object,
            "parent": node.parent_bus.name,
        }

    for link in d_overheadline:
        pgObj[link.gld_index] = {
            "id": link.id,
            "gldIndex": link.gld_index,
            "name": link.name,
            "object": link.object,
            "from": link.from_bus.name,
            "to": link.to_bus.name,
        }


    for link in d_undergroundline:
        pgObj[link.gld_index] = {
            "id": link.id,
            "gldIndex": link.gld_index,
            "name": link.name,
            "object": link.object,
            "from": link.from_bus.name,
            "to": link.to_bus.name,
        }


    for link in d_regulator:
        pgObj[link.gld_index] = {
            "id": link.id,
            "gldIndex": link.gld_index,
            "name": link.name,
            "object": link.object,
            "from": link.from_bus.name,
            "to": link.to_bus.name,
        }


    for link in d_transformer:
        pgObj[link.gld_index] = {
            "id": link.id,
            "gldIndex": link.gld_index,
            "name": link.name,
            "object": link.object,
            "from": link.from_bus.name,
            "to": link.to_bus.name,
        }


    for link in d_switch:
        pgObj[link.gld_index] = {
            "id": link.id,
            "gldIndex": link.gld_index,
            "name": link.name,
            "object": link.object,
            "from": link.from_bus.name,
            "to": link.to_bus.name,
        }

    data = pgObj
    with open("data/omf_data" + ".json", "w") as outFile:
        json.dump(data, outFile, indent=4)
    return data