# -*- coding: utf-8 -*-
"""
--- 当年万里觅封侯，匹马戍梁州。---

HH 私人订制Python开发库 -- 文件处理开发库 --

1，文件处理开发库
基准库数据处理接口库：
数据文件处理，csv,txt,excel.处理成 xy train test数据。对数据处理结果进行输出层csv txt excel数据。
数据处理对来自于数据库的或者api json/xml等的格式输入输出处理。
接口API封装开发。

2，算法库：
各种算法封装为 fit, score, result。 参数设定输入。

3，算法整合库，自动调参：
对参数的自动校正，根据结果评判，自动调参。输出最优化的模型和参数设置

Created on Thu Nov 22 09:36:45 2018
@author: hushenghua
"""

'''
#Python Pandas DataFrames
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
pandas.read_csv, pandas.read_table, pandas.read_clipboard
'''


import pandas as pd
#import os
import matplotlib.pyplot as plt

#load data from a file
def load_file_data(filename):
    dataset = pd.read_excel(filename)
    return dataset

#test    
dataset = load_file_data(r'F:\Dev\HH_Python\HH_Lib\data\test_data_title.xlsx')   
#print(dataset.shape)    #size, rows, columns
#print(dataset.head())   #top 5 rows of data
#print(dataset.tail())   #last 5 rows
#print(dataset.dtypes)   #check the types of each column
#print(dataset['销售物业毛利率（%）'].astype(int))   #change the datatype of a specific column, use the .astype() function.
#print(dataset['销售物业毛利率（%）'].describe())    #to see some of the core statistics about a particular column, you can use the ‘describe‘ function.
#print(dataset['销售物业毛利率（%）'][3:5])


# Series summary operations.
# We are selecting the column "Y2007", and performing various calculations.
'''
print([dataset['销售物业毛利率（%）'].sum(), # Total sum of the column values
 dataset['销售物业毛利率（%）'].mean(), # Mean of the column values
 dataset['销售物业毛利率（%）'].median(), # Median of the column values
 dataset['销售物业毛利率（%）'].nunique(), # Number of unique entries
 dataset['销售物业毛利率（%）'].max(), # Maximum of the column values
 dataset['销售物业毛利率（%）'].min()]) # Minimum of the column values
'''
#print(dataset[['销售物业毛利率（%）','土地款支付节奏（天）']].describe()) 
    
print(dataset.iloc[10:20,1:3])    #the iloc and loc selection 

#output file: to_csv , and to_excel 
#dataset.iloc[10:20,1:3].to_csv(r'F:\Dev\HH_Python\HH_Lib\data\output.csv', index=False, encoding='gbk')
#dataset.iloc[10:20,1:3].to_excel(r'F:\Dev\HH_Python\HH_Lib\data\output.xlsx', sheet_name="Sheet 1", index=False)

dataset.iloc[10:20,1:3].plot(kind='hist',bins=100)
plt.xlabel('xlabel')
plt.ylabel('ylabel')

print("done")

    
