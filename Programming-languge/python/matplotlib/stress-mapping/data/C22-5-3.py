# -*- coding: utf-8 -*-
"""
Created on Wed May  3 21:13:40 2023

@author: shiduyule
"""

from fu import enhanceresolution as er
import numpy as np
#print(np.around(np.linspace(0,156,19)))
# 一共有14个视频   行数必须是14行  
data2d = np.array([
# cy   cy     注意 右旋为正  还是左旋为负

#1    2    3    4     5    6     7     8     9    10    11    12    13    14     15   
#   17
[0,   0,   0,   0,    0,   0,    0,    0,    0,    0,   0,    0,    0,    0,     0,],

#   19
[0,   0,   0,   0,    0,  -2,    0,    0,    0,    0,   0,    0,    0,    0,     0,],

#   21
[0,   0,   0,   0,   -2, -1,    0,    0,    0,    0,  1.5,   0,    0,    0,     0,],

#   23
[0,   0,   0, -1.6, -3,  -2,    0,    0,    0,    0,   0,  0.5,   0,     0,     0,],

#   25
[0,   0, -0.5,  -2,  -2.9,-2.2,   0,    0,    0,    0,   0,  1.5,   0,     0,     0, ],

#   27
[0,   0,   0,   0,  -1.6,-2.2,  -2.4,  0,    0,    0,   0,   0,    0,     0,     0  ],

#   29
[0,   0,   0,   0,    0,   0,    0,    0,   -2,   -0.8,   0,  0.2,    0,    0,     0  ],

#   31
[0,   0,   0,   0,    0,   0,    0,   -1,  -3.8,   0,   0,    0,    0,    0,     0,],

#   33
[0,   0,   0,   0,  2.5,   4,    0,    0,    0,  -0.8,   0,    0,    0,    0,     0, ],

#   35
[0,   0,   0,   0,  2.4,   0,    0,    0,    0,  -1.8,-1.5,  -2,   -1,   -1.4,   -1,],

#    37
[0,   0,   0,   0,   0,    0,    0,    0,    0,  -0.2, -2,    0,   0,     0,      0],

#     39
[0,   0,   0,   0, 0.1,    0,    0,    0,    0,  -0.1, -2,   -3,  -2.2, -1.8,    0.6],

#     41
[0,   0,   0,   0,  0,     0,    0,    0,    0,  -0.1,-1.5,  -1.9,-1.8,   0,      0],

#     43
[0,   0,   0,   0,    0,   0,    0,    0,    0,    0,  -0.5,  -2,   0,   -1,      0]


]  )

data2d =  0.1414 * data2d 
data2d = er(data2d,3.5,3.3,'C1')    