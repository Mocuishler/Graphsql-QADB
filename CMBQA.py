#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import csv

global norepeatdata
norepeatdata = []

Address = os.getcwd()
print Address



objectlist = []
filename = ["Agent_Action.csv", "Argument_Attrib.csv", "Dative_Action.csv", "Field_Attrib.csv", "Objective_Clause.csv",
            "Patient_Action.csv"]
# for i in range(0, 6):
#     with open(filename[i], 'r') as f:
#         final_data = []
#         reader = f.read(-1)
#         data_lis = reader.split('\n')
#         for i in data_lis:
#             tmp = i.split(' ')
#             final_data.append(tmp)
#         for i in final_data:
#             if len(i) >= 2:
#                 if i[3] not in norepeatdata:
#                     norepeatdata.append(i[3])
#         f.close()
# print
# print norepeatdata
# for i in norepeatdata:
#     print i
objname = "操作,转账,账,时间,模式,账户,汇款,网上,什么,号码,具体,手机,信用卡,大额,普通,长,异地,跨行,非,实时,银行,个人,网络"
actname = "到,功能,银行,账,号码,是,转账,进行,选择,汇款,模式,具体,跨行,长,普通,时间,手机,异地,实时,网上,开始,网络,操作,账户,什么"
aswlist = ['2', '3', '4', '5', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '1']

