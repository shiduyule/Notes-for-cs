# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:41:06 2023

@author: shiduyule
"""
from fu import enhanceresolution as er
import numpy as np
#print(np.around(np.linspace(0,156,19)))
# 一共有18个视频  行数定死了是19行  
data2d = np.array([
# cy   cy     注意 右旋为正  还是左旋为负
[0,   0,   0,   0,    0,   0,    0,    0,    0,    0,    0,    0,    2,    3,    1,    0,    -1,   ],
[0,   0, -0.5,  0,    0,   0,    0,    0,    0,  0.5,    1,    2,    3,    3,    2,    0,     0,   ],
[0,   0,   0,  -0.5,  0,  -0.5,-0.5,   0,    0,  0.5,    2,    3,    4,    3,   -1,    0,     0,   ],
[0,   0,   0,  -1,    0,   0,    0,    0,    0,    1,    2,    3,   3.5,   0,    0,    0,     0,   ],
[0,  -0.5,-0.5,-0.5,  0,   0,    0,    0,    0,    0,    0,    0,    2,    0,    1,    1,     0,   ],
[-1,  -1,  0,   0,    0,   0,    0,    0,    0,    0,    0,     1,  2.5,   2,    2,    1,     0,   ],
[-1,  -1,  0,   0,    0,   0,   -1,   -1,    0,    0,    1,    2,    2,    3,    3,    2,     0]  ,
[-1,  -1,  0,  -1,    0,   0,    0,   -1,    0,    0,    1,    1,    0,    2,    3,    1,     1],
[0,    0,  0,  -0.5,  0,   0,  -0.5,  -2,    2,    0,    0,    0,    0,    1,    1,    1,     1],
[0,    0,  0,   0,    2,   0,    0,    -1,   0,    0,    0,    -2,   0,    1,    0,    0,     0,],
[0,    0,2.6,  2.5, 2.1, 2.9,   1.8,  3.4,   -3,  -3.2,    -1,   -1,   -3,  -3,    0,    0,     0,],

[0,    1,  2,   3,   3,   1,    1,    0,    -1,    0,    0,   -0.5, -2.8, -2.5, -0.5,   0,     0 ],

[0,    0,  1,  2.5,   3,   0,    0,    0,     0,    0,    0,    -1,  -2,   -1.5,  0,    0,     0],
[0,    0,  0,  0.2,  0.5, -0.5,    0,    0,     0,    0,    1,    1,    0,   -1,    0,    0,     0],
[0,    0, -1,  -0.5,   0,   0,    0,    0,     0,    2,    2,    3,    1,    0,    1,   1,      0],

[-3,  -3.5,-4,-2.5,  -1,  0,    0,    0,     0,    1,    2,    3,    3,    3,    3,    2,     2],
[0,   -4,  -3,  -2,  -1,  -1,   0,   -0.5,   0,    0,    0,    2,    3,    4,   4.1,   2,      1]

])#                                                                                                     右下角数据缺失

data2d =  0.1414 * data2d 
data2d = er(data2d,4.2,3.8,'B1')