# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:33:42 2022

@author: USER
"""

import requests #上網用

import json #解析JSON格式

url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=700"

bike=requests.get(url).text

data = json.loads(bike)

area={}
snA={}
sbI={}
bemP={}
for row in data:
    if not(row["sarea"] in area):
        
        area[row["sarea"]]=[]
        area[row["sarea"]].append(row)
print(area.keys())

input('請輸入地區: ')

for row  in data:
    if not(row["sna"] in snA):
        snA[row["sna"]]=[]
        snA[row["sna"]].append(row)
print('以下為站名',snA.keys())

for row  in data:
    if not(row["sbi"] in sbI):
        sbI[row["sbi"]]=[]
        sbI[row["sbi"]].append(row)
print('可借為',sbI.keys(),'輛')

for row  in data:
    if not(row["bemp"] in bemP):
        bemP[row["bemp"]]=[]
        bemP[row["bemp"]].append(row)
print('可停為',bemP.keys(),'輛')


#作業:由使用者輸入上面其中一個地區程式要印出該區所有站名，可借，可停的資料。


    # print(row['sna'])
    # print(row['sbi'])
    # print(row['bemp'])
    # print(row['*'*50])




