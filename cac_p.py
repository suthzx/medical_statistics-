#!/usr/bin/env python
# coding: utf-8
# thsu0407@gmail.com
import numpy as np
import pandas as pd
from scipy import stats
import itertools
def get_p_value(arrA,arrB):
    a = np.array(arrA)
    b = np.array(arrB)
    t, p = stats.ttest_ind(a,b)
    return p
def get_sheet(path='STH1.xlsx'):
    import openpyxl
    wb = openpyxl.load_workbook(path)
    # 获取workbook中所有的表格
    sheets = wb.sheetnames
    return sheets
def cac_zx(s,index1=0,index2=1):
    index1 = index1
    index2 = index2
    a = np.array(df[s[index1]].dropna())
    b = np.array(df[s[index2]].dropna())
    #print(s[index1],a)
    #print(s[index2],b)
    #print ("p_value",get_p_value(a,b))
    return s[index1],s[index2],get_p_value(a,b)

sheet = get_sheet("./zxp.xlsx")
df = pd.read_excel(io="./zxp.xlsx",sheet_name=sheet[-1])
com = [x for x in df.columns]

s1 = []
s2 = []
s3 = []
s4 = []
for i in com:
    if "S1" in str(i)[:2]:
        s1.append(i)
for i in com:
    if "S2" in str(i)[:2]:
        s2.append(i)
for i in com:
    if "S3" in str(i)[:2]:
        s3.append(i)
for i in com:
    if "S4" in str(i)[:2]:
        s4.append(i)

data= pd.DataFrame()
c1 = []
c2 = []
pv = []
for s in [s1,s2,s3,s4]:
    s = s
    print(s)
    # get sheet number
    list1 = [x for x in range(len(s))]
    index_list= list(itertools.combinations(list1,2))
    print(len(index_list))
    for i in index_list:
        result = cac_zx(s=s,index1=i[0],index2=i[1])
        print(result[0])
        c1.append(result[0])
        c2.append(result[1])
        pv.append(result[2])
    
data["c1"] = c1
data["c2"] = c2
data["pv"] = pv


data.to_csv("zxcp.csv",index = None)



