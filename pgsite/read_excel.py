import pandas as pd
import sys
import os
from distribution.models import Feeder, D_Bus, D_Load, D_Capacitor
from distribution.models import D_OverheadLine, D_UndergroundLine, D_Regulator, D_Transformer, D_Switch
from distribution.models import D_Generator, D_Storage, D_Solar
# D_Solar_TIMEDATA
# D_Load_TIMEDATA

fileDir = "./excel"


feederName = "Circuit01"
fname = feederName + ".xlsx"

if Feeder.objects.filter(name = feederName).count() > 0:
	feeder = Feeder.objects.get(name = feederName)
	print 'Get from db'
else:
	feeder = Feeder.objects.create(name=feederName)
	print 'Create new Feeder', feederName

print os.path.join(fileDir, fname)
try:
	xl = pd.ExcelFile(os.path.join(fileDir, fname))
	print 'Find the excel file!!!'
except:
	print "No excel file"
	quit()

# Get bus info
print '------------read bus-------------'


try:
	df = xl.parse("buses",header=None)
except:
	print "No bus info"
	quit()

nbuses = int(df.iat[0,1])
print 'number of buses', nbuses
busname = []
buslat = []
buslon = []
nominalVolt = []

for i in range(nbuses):
	val = str(df.iat[3+i,0])
	busname.append(val)
	val = float(df.iat[3+i,1])
	buslat.append(val)
	val = float(df.iat[3+i,2])
	buslon.append(val)
	val = float(df.iat[3+i,3])
	nominalVolt.append(val)
print '---makedb bus----'
for i in range(len(busname)):
	if feeder.d_buses.all().filter(name=busname[i]).count() == 0:
		print 'create bus'

		D_Bus.objects.create(
			name=busname[i],
			# pgIndex = currRelated,
			object = "node",
			feeder = feeder,
			nominal_voltage = nominalVolt[i],
			lat = buslat[i],
			lng = buslon[i]
		)
	else:
		print 'already in db', busname[i]

# Get lines info
print '----------read lines-----------'
try:
	df = xl.parse("lines",header=None)
except:
	print "No lines info"
	quit()
nlines = int(df.iat[0,1])
linename = []
linefrom = []
lineto = []
# linecap = []
# linebmat = []

for i in range(nlines):
	val = str(df.iat[3+i,0])
	linename.append(val)
	val = str(df.iat[3+i,1])
	linefrom.append(val)
	val = str(df.iat[3+i,2])
	lineto.append(val)
	# val = float(df.iat[3+i,3])
	# linecap.append(val)
	# val = float(df.iat[3+i,4])
	# linebmat.append(val)

print '----------makedb lines-----------'
from collections import Counter
print [k for k,v in Counter(linename).items() if v > 1]



regcount = 0
transcount = 0
swcount = 0
ovcount = 0
for i in range(len(linename)):
	if 'REG' in linename[i]:
		if feeder.d_regulators.all().filter(name=linename[i]).count() == 0:
	
			print 'create regulator'
			regcount += 1
			D_Regulator.objects.create(
				name=linename[i],
				# pgIndex = currRelated,
				fromWhere = D_Bus.objects.get(name=linefrom[i]),
				toWhere = D_Bus.objects.get(name=lineto[i]),
				feeder = feeder,
				# capacity = linecap[i],
				# bmat = linebmat[i]
			)
		else:
			'already in db'
	elif 'SW' in linename[i]:
		if feeder.d_switches.all().filter(name=linename[i]).count() == 0:
	
			print 'create switch'
			swcount += 1
			D_Switch.objects.create(
				name=linename[i],
				# pgIndex = currRelated,
				fromWhere = D_Bus.objects.get(name=linefrom[i]),
				toWhere = D_Bus.objects.get(name=lineto[i]),
				feeder = feeder,
				# capacity = linecap[i],
				# bmat = linebmat[i]
			)
		else:
			'already in db'
	elif 'Transformer' in linename[i]:
		if feeder.d_transformers.all().filter(name=linename[i]).count() == 0:
	
			print 'create transformer'
			transcount += 1
			D_Transformer.objects.create(
				name=linename[i],
				# pgIndex = currRelated,
				fromWhere = D_Bus.objects.get(name=linefrom[i]),
				toWhere = D_Bus.objects.get(name=lineto[i]),
				feeder = feeder,
				# capacity = linecap[i],
				# bmat = linebmat[i]
			)
		else:
			'already in db'
	else:
		if feeder.d_overheadlines.all().filter(name=linename[i]).count() == 0:
	
			print 'create overheadline'
			ovcount += 1
			D_OverheadLine.objects.create(
				name=linename[i],
				# pgIndex = currRelated,
				fromWhere = D_Bus.objects.get(name=linefrom[i]),
				toWhere = D_Bus.objects.get(name=lineto[i]),
				feeder = feeder,
				# capacity = linecap[i],
				# bmat = linebmat[i]
			)
		else:
			'already in db'

print 'ovcount', ovcount, 'swcount', swcount, 'regcount', regcount, 'transcount', transcount

# Get price info
# print '----------read price-----------'
# try:
# 	df = xl.parse("price",header=None)
# except:
# 	print "No price info"
# 	quit()
# nperiods = int(df.iat[0,1])
# price = []
# for i in range(nperiods):
# 	val = float(df.iat[3+i,1])
# 	price.append(val)

# Get generator info
print '----------read generators-----------'
try:
	df = xl.parse("generators",header=None)
except:
	print "No generator info"
	quit()
ngens = int(df.iat[0,1])
genname = []
gencost = []
gencap = []
genloc = []
for i in range(ngens):
	val = str(df.iat[3+i,0])
	genname.append(val)
	val = float(df.iat[3+i,1])
	gencost.append(val)
	val = float(df.iat[3+i,2])
	gencap.append(val)
	val = str(df.iat[3+i,3])
	genloc.append(val)

print '----------makedb generators-----------'


for i in range(len(genname)):
	if feeder.d_generators.all().filter(name=genname[i]).count() == 0:

		print 'create generator'
		D_Generator.objects.create(
			name=genname[i],
			# pgIndex = currRelated,
			feeder = feeder,
			parentLocation = D_Bus.objects.get(name=genloc[i]),
			capacity = gencap[i],
			cost = gencost[i],
		)
	else:
		print 'already in db'

# Get storage info
print '----------read storage-----------'
try:
	df = xl.parse("storages",header=None)
except:
	print "No storage info"
	quit()
nstrgs = int(df.iat[0,1])
strgname = []
strgminchrg = []
strgmaxchrg = []
strgintchrg = []
strgchrgrt = []
strgdischrgrt = []
strgchrgeff = []
strgdischrgeff = []
strgloc = []
for i in range(nstrgs):
	val = str(df.iat[3+i,0])
	strgname.append(val)
	val = float(df.iat[3+i,1])
	strgminchrg.append(val)
	val = float(df.iat[3+i,2])
	strgmaxchrg.append(val)
	val = float(df.iat[3+i,3])
	strgintchrg.append(val)
	val = float(df.iat[3+i,4])
	strgchrgrt.append(val)
	val = float(df.iat[3+i,5])
	strgdischrgrt.append(val)
	val = float(df.iat[3+i,6])
	strgchrgeff.append(val)
	val = float(df.iat[3+i,7])
	strgdischrgeff.append(val)
	val = str(df.iat[3+i,8])
	strgloc.append(val)
print '----------makedb storage-----------'


for i in range(len(strgname)):
	if feeder.d_storages.all().filter(name=strgname[i]).count() == 0:

		print 'create storage'
		D_Storage.objects.create(
			name=strgname[i],
			# pgIndex = currRelated,
			parentLocation = D_Bus.objects.get(name=strgloc[i]),
			feeder = feeder,
			minCharge = strgminchrg[i],
			maxCharge = strgmaxchrg[i],
			initialCharge = strgintchrg[i],
			chargeRate = strgchrgrt[i],
			dischargeRate = strgdischrgrt[i],
			chargeEff = strgchrgeff[i],
			dischargeEff = strgdischrgeff[i],
		)
	else:
		print 'load in db'


# Get renewables info
print '----------read renewables-----------'
try:
	df = xl.parse("renewables",header=None)
except:
	print "No renewables info"
	quit()
nrens = int(df.iat[0,1])
renname = []
renloc = []

for i in range(nrens):
	val = str(df.iat[3+i,0])
	renname.append(val)
	val = str(df.iat[3+i,1])
	renloc.append(val)

print '----------makedb renewables-----------'


for i in range(len(renname)):
	if feeder.d_solars.all().filter(name=renname[i]).count() == 0:

		print 'create solar'
		D_Solar.objects.create(
			name=renname[i],
			# pgIndex = currRelated,
			parentLocation = D_Bus.objects.get(name=renloc[i]),
			feeder = feeder,
		)
	else:
		print 'load in db', renloc[i]

# Get loads  info
print '----------read load--------------'
try:
	df = xl.parse("loads",header=None)
except:
	print "No loads info"
	quit()
nloads = int(df.iat[0,1])
loadname = []
loadloc = []

for i in range(nloads):
	val = str(df.iat[3+i,0])
	loadname.append(val)
	val = str(df.iat[3+i,1])
	loadloc.append(val)

print '----------makedb load--------------'


for i in range(len(loadname)):
	if feeder.d_loads.all().filter(name=loadname[i]).count() == 0:

		print 'create load'
		D_Load.objects.create(
			name=loadname[i],
			# pgIndex = currRelated,
			object = "load",
			parentLocation = D_Bus.objects.get(name=loadloc[i]),
			feeder = feeder
		)
	else:
		print 'load in db'