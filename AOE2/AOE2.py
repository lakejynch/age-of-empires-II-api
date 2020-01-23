import python
import os
import time
import json
import csv

civs = ["Aztecs","Berbers","Britons","Bulgarians","Burmese","Byzantines","Celts","Chinese","Cumans","Ethiopians","Franks","Goths","Huns","Incas","Indians","Italians","Japanese","Khmer","Koreans","Lithuanians","Magyars","Malay","Malians","Mayans","Mongols","Persians","Portuguese","Saracens","Slavs","Spanish","Tatars","Teutons","Turks","Vietnamese","Vikings"]

villagers = 3
popTotal = 5
popCount = villagers + 1

lumberRt = 23.28
shepRt = 19.80
gathRt = 18.60
fishRt = 25.56
huntRt = 24.48
farmRt = 19.14
stoneRt = 21.54
goldRt = 22.74
tps = 0.8 #tiles per second

startTime = 0.000
vilTime = 25.000

