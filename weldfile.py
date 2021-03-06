import re
from pandas import Series, DataFrame

import os

targetFiles = []
listLineID = []
listPipingSpec = []
listWeldNo = []
listCat = []
listSize = []
listType = []
listTempQtyChk = []

for file in os.listdir("d:\\w1"):
    tempFileSpilt = file.split('.')
    lenFileSplit = len(tempFileSpilt)
    tempFileEx = tempFileSpilt[lenFileSplit-1]
    
    if bool(re.match('^w\d{1,2}$', tempFileEx)):
        targetFiles.append(os.path.join("d:\\w1", file))

for targetFile in targetFiles:
    with open(targetFile, 'r') as file:
        lines = file.readlines()
        line = ''

        for line in lines:
            line = line + '                                  '
            if line.find('PIPELINE REF',0,15)>=0:
                wLineID = line.split(':-')[1].strip()
            if line.find('PIPING SPEC',0,13)>=0:
                wPipingSpec = line.split(':-')[1].strip()

            if bool(re.match('^\d{1,2}$', line[0:5].strip())):
                wNo = line[2:4].strip()
                wCat = line[19:22].strip()
                wSize = line[25:32].strip()
                wType = line[32:43].strip()

                listLineID.append(wLineID)
                listPipingSpec.append(wPipingSpec)
                listWeldNo.append(wNo)
                listCat.append(wCat)
                listSize.append(wSize)
                listType.append(wType)
                listTempQtyChk.append(wCat+wPipingSpec+wSize+wType+wLineID)


data = {'TempQtyChk': listTempQtyChk,
        'PipeID': listLineID,
        'PipingSpec': listPipingSpec,
        'WeldCat': listCat,
        'WeldSize': listSize,
        'WeldType': listType}
weldDF = DataFrame(data).groupby(['PipeID','PipingSpec','WeldCat','WeldSize','WeldType']).agg({'TempQtyChk':'count'}).rename(columns={'TempQtyChk':'WeldPoint'}).reset_index()
