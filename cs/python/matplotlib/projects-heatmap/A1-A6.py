# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 22:19:47 2023

@author: shiduyule
"""

import matplotlib.pyplot as plt
import numpy as np



fig, axs = plt.subplots(2, 2)  # 将两行两列的图像
cmaps = ['RdBu_r', 'viridis']
for col in range(2):
    for row in range(2):
        ax = axs[row, col]
        pcm = ax.pcolormesh(np.random.random((20, 20)) * (col + 1),
                            cmap=cmaps[col])
        fig.colorbar(pcm, ax=ax)
        