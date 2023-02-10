# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:57:45 2023

@author: shiduyule
"""

import numpy as np

filename = '1-M.txt'
newlist = np.array([])
with open(filename, 'r') as file:  #  打开txt文件 将它赋值给file
    counts = 343
    newline =  1
    while True:
        line = file.readline(counts)
        #print (line)
        newlist[newline] = line 
        counts =  counts + 593
        newline =  newline + 1
        if counts >= 1391179:
            break
        
 #  line = file.readline() # file.readline()会读取文件的第一行生成字符串类型的变量