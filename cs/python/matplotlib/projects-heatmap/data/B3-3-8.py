# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:07:25 2023
9 : 00
@author: shiduyule
"""

from fu import enhanceresolution as er
import numpy as np
#print(np.around(np.linspace(0,156,19)))
# 一共有19个视频  行数定死了是19行  
data2d = np.array([
# cy   cy     注意 右旋为正  还是左旋为负
[0,   0,   0,  -1,   -3,  -5.5,  -6.5,   -7,   -7,   -6,   -3,   0,   3,   4,   1,   0,   -2,   -4,  -1,   0],
[0,   0,   0,   2,   -1,   -4,    -5,    -7,   -7,   -6,   -4,   0,   3,   4,   3,   0,   -2,   -5,  -4,   0],
[0,  -1,  -1,   0,   -4,   -5,    -6,    -8,   -7,   -5,    0,   3,   4,   4,   2,   0,   -3,   -4,  -2,   0],
[0,  -2,  -5,  -5,   -6,   -7,    -8,    -9,   -8,   -6,   -4,   2,   4,   6,   5,   3,    0,  -0.5,  0,   0],
[0,  -3,  -4,  -5,   -7,   -8,    -10,   -10,  -9,   -5,    0,   5,   7,   7,   5,   0,    0,    0,   0,   0],


[-2, -4,  -5,  -5,   -6,   -6,    -8,    -9,   -8,   -7,    0,   6,   8,   8,   3,   0,    0,    0,   0,   0],
[-3, -4,  -5,  -4,   -5,   -6,    -7,   -11,   -9,   -7,    0,   7,   9,   8, 3.5,   0,    0, -0.5,   0,   0],

[-3, -4,  -4.5,-5,   -5,   -4,    -5,   -9,    -9,   -8,    0,   8,   7, 7.5,  0,  -0.5,  -3, -4.5,  -4.5, -4],

[-3, -3, -3.5, -3.5, -4,   -4,    -3,   -5,    -6.5, -7,   -4,   8,  10,  4,  -4,   -5,    -7,  -8,   -8,  -7],

[-2, -1,  -2,  -1,   0,    0,     0,    -1,   2.5,    6,    8,   6,   4,  0,  -9,   -10, -10,  -10,   -9,  -8],
[-1, -1,  -1,  -1,   0,   -2,     3,    4,     8,    12,    6,  -9,  -9, -8,  -7,  -8,   -8,   -8,    -7,  -6],
[0, -1,  -1,   -1,  -1,   -2,     1,    3,     6,     9,    5,  -8, -10, -8,  -6,  -5,   -5,  -5,     -5,  -5],
[0, 0,    0,    0,  0,     2,     4,    5,     3,    3.5,   0,  -9,  -11, -8,  -6, -4,   -4,   -3,   -2,    0],
[0,  0,  0,    0,   1,    3,      4,  4.5,     3,     0,   -5, -6.5,  -9, -9, -6,  -4,   -3,   0,     0,    0],
[0, 0,   0,    0,   2,    5,     4,     3,    -2,    -8,   -8,   -9,  -8, -5, -2,   0,    0,    0,    0,    0],
[0, 0,   0,    -2,  0,    3,     4,     4,     3,     0,  -6.5,  -7,  -8,-8,  -7,  -4,    0,   1,     2,    2],

[0, -1,  -2,   -4,  0,    2,     4,     4,   2.5,     0,   -6,   -7,  -8, -7, -4,   -1,   4,   4,     3,    3],
[0, -1,  -3,   0,   0,    1,     3,     2,    2,     -1,   -5,   -6,  -7, -7,  -4.5,-1,   2,   6,    6,     4],

[0,  0,  -1,  0,    0,    0,     1,     1,     0,    -3,   -6,   -7,  -7, -6,  -3,  0,    4,   5,    5,     5],
[0,  0,   0,  0,    2,    3,     3,     3,    3,      0,   -3,   -4,  -5, -4,  -1,  0,    2,   4,    3,     2]
])#                                                                                                     右下角数据缺失

data2d =  0.01414 * data2d 
data2d = er(data2d,4.5,4.5,'B3')