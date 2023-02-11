# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:57:45 2023

@author: shiduyule
"""

#import numpy as np
import linecache
filename = ('1-M.txt')
line = 343
newline = 0
data = []
while True:
    if line >= 1391179:
        break
    data.append(linecache.getline(filename,line ))
    line += 593




for foo in data:
    #if foo[0] == 'ID' and foo[1] == "46": #条件
        with open('newfile.txt', 'w') as fp:　  
            # 'a'表示写的时候不覆盖原先内容，追加模式
            fp.write(foo[]) #读取指定内容
            fp.write('\n')
       
        with open('./file2.txt', 'a') as fp:
            fp.write(foo[7]) #读取指定内容
            fp.write('\n')

 #  line = file.readline() # file.readline()会读取文件的第一行生成字符串类型的变量