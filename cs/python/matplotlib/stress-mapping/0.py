# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:46:21 2022

@author: shiduyule
"""
import matplotlib.pyplot as plt  
import numpy as np
#%% 矩阵输入 matrix input
# =============================================================================
# 利用numpy中的二维数组作为容器  首先手动输入光轴倾角的数据  10 * 10 
# =============================================================================
data2d = np.array([
[-1,   0.5, 0,  0.5, 1],
[0.8, 0.5, 0.4,  0.5, 0.8],
[0.6, 0.4, 1,  0.4, 0.6],
[0.8, 0.5, 0.3,  0.5, 0.8], 
[1,   0.5, 0,  0.5, 1]  ])

def function_distance_theta(x):   # x 是形式参数 data2d是实际参数
    y = 81
    theta = np.arctan(x/y)
    degree = np.degrees(theta)  # 弧度制转角度制
    return (degree)
print(function_distance_theta(data2d))