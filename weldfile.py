import re
from pandas import Series, DataFrame

import os
for file in os.listdir("d:\\w1"):
    if file.endswith(".w1"):
        print(os.path.join("d:\\w1", file))


listLineID = []
listPipingSpec = []
listWeldNo = []
listCat = []
listSize = []
listType = []
listTempQtyChk = []



with open('D:\\w1\\a.w2', 'r') as file:
    lines = file.readlines()
    line = ''

    for line in lines:
        line = line + '                                  '
        if line.find('PIPELINE REF',0,15)>=0:
            wLineID = line.split(':-')[1].strip()
        if line.find('PIPING SPEC',0,13)>=0:
            wPipingSpec = line.split(':-')[1].strip()

        if bool(re.match('\d[0-9 ]', line[2:4])):
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
            
    
    data = {'PipeID': listLineID,
            'PipingSpec': listPipingSpec,
            'WeldNo': listWeldNo,
            'WeldCat': listCat,
            'WeldSize': listSize,
            'WeldType': listType}
    wdd = DataFrame(data)
    wdd
            





            
        


