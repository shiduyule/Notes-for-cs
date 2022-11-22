# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt  
import numpy as np



t = np.linspace(0, 2 * np.pi, 1024)  # t的取值范围是(0,2π) 像素点是1024
b = np.sin(t)[:, np.newaxis]
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :] # 矩阵化


#%% 创建画布
fig, ax = plt.subplots(facecolor='#F5F5EB')  # 等价于 plt.subplots(1,1) 创建画布fig 和一个子区域

im = ax.imshow(data2d)          

#%% 追加图例
ax.set_title('Pan on the colorbar to shift the color mapping\n'
             'Zoom on the colorbar to scale the color mapping')

fig.colorbar(im, ax=ax, label='Interactive colorbar')  

plt.show()
