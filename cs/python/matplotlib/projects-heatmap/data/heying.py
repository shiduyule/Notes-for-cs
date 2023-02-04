# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 21:28:26 2023

@author: shiduyule
"""
import matplotlib.pyplot as plt
import numpy as np


# Fixing random state for reproducibility
np.random.seed(19680801)

fig, axs = plt.subplots(2, 2)
cmaps = ['RdBu_r', 'viridis']
for col in range(2):
    for row in range(2):
        ax = axs[row, col]
        pcm = ax.pcolormesh(np.random.random((20, 20)) * (col + 1),
                            cmap=cmaps[col])
        fig.colorbar(pcm, ax=ax)
      
'''        
plt.rcParams['savefig.dpi'] = 300 #图片像素 
plt.rcParams['figure.dpi'] = 300 #分辨率 
fig = plt.figure() 
fig, axes = plt.subplots(nrows=2, ncols=2) 
# plt.subplots 可以创建一个新的Figure 两行，两列4个画板 
axes[0,0].set(title='Upper Left') 
axes[0,1].set(title='Upper Right') 
axes[1,0].set(title='Lower Left') 
axes[1,1].set(title='Lower Right') 
'''