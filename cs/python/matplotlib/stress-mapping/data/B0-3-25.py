# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 15:56:19 2023

@author: shiduyule
"""


from fu import enhanceresolution as er
import numpy as np
#print(np.around(np.linspace(0,156,19)))
# 一共有19个视频  行数定死了是19行  
#0     9.    17.   26.   35.   43.   52.         1.    9.   18.   27.  35.  44.  53.    1.    10     19.   27.   36
data2d = np.array([
# cy   cy     注意 右旋为正  还是左旋为负
#1   2     3    4     5    6    7     8     9    10     11     12   13   14    15    16  17   18    
[4,  7,    6,   6,   6.5,  4,   3,    1,    0,  -4,     -9,    ]

])#                                                                                                     右下角数据缺失

data2d =  0.1414 * data2d 
data2d = er(data2d,4.8,4.2,'B2')