#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess
import json

global Theresult
global vertexslist
global v_type
global relationship
global FinalDictyonary

FinalDictyonary = {}
Theresult = []
vertexslist = ['转账','跨行','需要']
v_type = ['action','object','action']
relationship = ['Action_Modify','Agent_Action']

def cleanthevariable():
    vertexslist =[]
    v_type = []
    relationship = []

def printthevariable():
    print Theresult
    print vertexslist
    print v_type
    print relationship

def json_transform(sourcejson):

    the1json = json.loads(sourcejson)
    the2json = the1json["results"]
    dicdata = eval(the2json)
    return dicdata

# cleanthevariable()
#
# tempstring = raw_input("Input the vertexs name (Separated with comma):")
# vertexslist = tempstring.split(",")
# tempstring = raw_input("Input the vertexs type (Separated with comma):")
# v_type = tempstring.split(",")
# tempstring = raw_input("Input the relationship (Separated with comma):")
# relationship = tempstring.split(",")

for i in range(0,len(relationship)):
    k1 = vertexslist[i]
    k2 = vertexslist[i+1]
    k1_type =v_type[i]
    k2_type =v_type[i+1]
    rela =relationship[i]

    cmd ="curl -X GET 'http://127.0.0.1:9000/query/maroon2?k1=%s&k1.type=%s&k2=%s&k2.type=%s&rela=%s'"%(k1,k1_type,k2,k2_type,rela)
    p = subprocess.check_output(cmd, shell=True)

    dicr = json.loads(p)
    dicrr = dicr["results"]
    dicaa = dicrr[0]
    dicbb = dicaa["@@templist"]
    for i in dicbb:
        Theresult.append(int(i))

for i in Theresult:
        if i in FinalDictyonary:
            FinalDictyonary[i]+= 1
        else:
            FinalDictyonary[i]=1

ORDERDIC = sorted(FinalDictyonary.items(),key=lambda item:item[1],reverse=True)
print ORDERDIC[0:10]
Theresult=[]
cleanthevariable()