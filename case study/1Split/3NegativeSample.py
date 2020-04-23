from numpy import *
import numpy as np
import random
import math
import os
import time
import pandas as pd
import csv
import math
import random
import Tool
# 定义函数
def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:  # 把每个rna疾病对加入OriginalData，注意表头
        SaveList.append(row)
    return

def ReadMyCsv2(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        counter = 0
        while counter < len(row):
            row[counter] = int(row[counter])      # 转换数据类型
            counter = counter + 1
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return




MDCuiMiDiseaseNum = []
ReadMyCsv(MDCuiMiDiseaseNum, "MDCuiMiDiseaseNum.csv")
print('MDCuiMiDiseaseNum[0]', MDCuiMiDiseaseNum[0])
print('len(MDCuiMiDiseaseNum)', len(MDCuiMiDiseaseNum))

AllDiseaseNum = []
ReadMyCsv(AllDiseaseNum, "AllDiseaseNum.csv")         # 不使用下三角矩阵，无所为第一个数字大于第二个

AllMiNum = []
ReadMyCsv(AllMiNum, "AllMiNum.csv")         # 不使用下三角矩阵，无所为第一个数字大于第二个

print(AllMiNum[0])

import Tool
NegativeSample = Tool.NegativeGenerate(MDCuiMiDiseaseNum, AllDiseaseNum, AllMiNum)
Tool.StorFile(NegativeSample, 'NegativeSample.csv')

#NegativeSample.csv生成负样本
