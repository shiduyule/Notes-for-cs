# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:05:44 2024

@author: shiduyule
"""


from fu import enhanceresolution as er
import numpy as np

print(np.around(np.linspace(0,145,9)))
# 一共有18个视频  行数定死了是18行 

data2d = np.array([

[-1,  -0.8, -0.1,  0.2,  1.1,  1.2,  1.1,  0.2, -0.9 ],
[-0.3, 0.1,  0.1, -0.1,  0.5, 1.25, 1.15, 0.25,  0.1],
[-0.2,-0.1,  0.1,    0,  1.0,  1.5,  0.2,  0.3,  0.4],
[0.2, -0.1,  1.1,  0.2, -0.1,  0.0,  1.1,  1.2,  0.0], 
[0.3,  0.4,  0.1, -0.7,  0.2,  0.1,  0.2, -0.1,  0.2],
[0.2,  0.8,  0.5, -0.3, -0.1,  0.7,  0.0, -0.2,  0.0],
[0.8,  1.1,  0.9,  1.2,  0.2, -0.2, -0.1,  0.0,  0.0],
[-0.7, 0.4,  0.5,  0.9,  1.2,  0.0,  0.0,  1.0,  0.0],
[-0.9, 0.2,  0.3,  0.4,  1.3,  0.1, -0.5,  0.0,  -0.1]  ])

data2d =  0.1414 * data2d
data2d = er(data2d,4.0,3.5,'example')