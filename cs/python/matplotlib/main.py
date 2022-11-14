# -*- coding: utf-8 -*-
#%% 导入模块 import modules
import matplotlib.pyplot as plt  
import numpy as np


#%% 矩阵输入 matrix input
# =============================================================================
# 利用numpy中的二维数组作为容器  首先手动输入光轴倾角的数据  10 * 10 
# =============================================================================

t = np.linspace(0, 2 * np.pi, 1024)

data2d = np.array([
[1,   0.5, 0,  0.5, 1],
[0.8, 0.5, 0,  0.5, 0.8],
[0.6, 0.5, 0,  0.5, 0.6],
[0.8, 0.5, 0,  0.5, 0.8], 
[1,   0.5, 0,  0.5, 1]  ])

# 结果为二维数组
# data2d = np.random.random((10,10))
 


#%% 矩阵扩充  matrix expand 至少扩充到 100 * 100
hangshu = np.shape(data2d)[0]  #行数  
lieshu = np.shape(data2d)[1]  #列数

#=============================================================================
# 扩充列数
# =============================================================================
j = 0
i = 0
density = 10
insertcolumn = np.empty([np.shape(data2d)[0] ,density], dtype = float) 
print(insertcolumn)
# 插入的矩阵行数为data2d的行数  列数为设置的密度值
while lieshu < 100: # 当列数小于时
    while i < np.shape(data2d)[0]:  # 当行数在总行数范围内
        insertcolumn[i,:] = np.linspace(data2d[i,j],data2d[i,j+1],density,endpoint = False)[0:density] # 以第i行第j列 和第i行第j+1列为起始值   这里是 5行 10列数组
        i = i + 1 
        
    insertcolumn = insertcolumn.transpose()
    data2d = np.insert(data2d, j+1,insertcolumn, axis=1) # 插入density列
    j = j + 1 + density 
    lieshu = np.shape(data2d)[1]
    break
#=============================================================================
# 扩充行数
# =============================================================================
# =============================================================================
# j = 0
# i = 0
# density = 100
# insertline = np.empty([np.shape(density,data2d)[1]], dtype = float) 
# # 插入的矩阵行数为data2d的行数  列数为设置的密度值
# while np.shape(data2d)[1] < 10:
#     i = 0
#     while i < np.shape(data2d)[0]:  # 当l列数在总行数范围内
#         insertcolumn[i,:] = np.linspace(data2d[i,j],data2d[i+1,j],density,endpoint = False)[0:density]
#         i = i + 1 
#     insertcolumn = insertcolumn.transpose()
#     data2d = np.insert(data2d, i,insertcolumn, axis=0) # 插入一行
#     i = i + 1 + density 
# =============================================================================


#%% 矩阵转化 利用matlab中 拟合得到的函数
def function_theta_strain(x):
    a0 =   7.363e-05 
    a1 =  -8.187e-05 
    b1 =  -2.305e-05 
    a2 =   7.352e-06 
    b2 =   1.373e-05 
    a3 =   9.547e-07 
    b3 =  -1.768e-06 
    w =       1.798  
    S21output =  a0 + a1 * np.cos(x*w) + b1 * np.sin(x*w) + a2 * np.cos(2*x*w) + b2 * np.sin(2*x*w) + a3 * np.cos(3*x*w) + b3 * np.sin(3*x*w)
    return (S21output)

data2d = function_theta_strain(data2d)



#%% 创建画布
fig, ax = plt.subplots(facecolor='#F5F5EB')  # 等价于 plt.subplots(1,1) 创建画布fig 和一个子区域

im = ax.imshow(data2d)          

#%% 追加图例
ax.set_title('Pan on the colorbar to shift the color mapping\n'
             'Zoom on the colorbar to scale the color mapping')

fig.colorbar(im, ax=ax, label='Interactive colorbar')  

plt.show()