# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:57:45 2023

@author: shiduyule
"""

# import re  #     返回string中所有与pattern匹配的全部字符串,返回形式为数组
import linecache
filename = ('1-M.txt')
line = 343   #  输入 行数 周期
data = []   
while True:
    if line >= 663366:
        break
    data.append(linecache.getline(filename,line))
    line += 593   #  输入 周期



'''
#for foo in data:
    #if foo[0] == 'ID' and foo[1] == "46": #条件
with open('newfile.txt','a') as f:   # 'w'表示写的时候不覆盖原先内容，追加模式　  
    
    f.write(str(data)) #读取指定内容
            #fp.write('\n')
 #  line = file.readline() # file.readline()会读取文件的第一行生成字符串类型的变量
 
'''