# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:20:58 2024

@author: 代晓阳
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from chicun import changexy
#将颜色映射到 vmin~vmax 之间
norm = matplotlib.colors.Normalize(vmin=0, vmax=2.0e-5)

# 假设有五个数据集
# data1 = np.random.rand(10, 10)
# data2 = np.random.rand(10, 10)
# data3 = np.random.rand(10, 10)
# data4 = np.random.rand(10, 10)
# data5 = np.random.rand(10, 10)

# 创建一个 2x3 的子图布局，因为需要三个子图在第一行，两个子图在第二行
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(12, 8), dpi=600)

# 移除第二行的第三个子图
fig.delaxes(axs[1, 2])

# 画出每个数据集对应的子图
im1 = axs[0, 0].imshow(data1, origin='lower',norm=norm)
im2 = axs[0, 1].imshow(data2, origin='lower',norm=norm)
im3 = axs[0, 2].imshow(data3, origin='lower',norm=norm)
im4 = axs[1, 0].imshow(data4, origin='lower',norm=norm)   
im5 = axs[1, 1].imshow(data5, origin='lower',norm=norm)

# 设置公共的标签和刻度
for ax in axs.flat:
    ax.set_xlabel('Size (cm)', fontdict={"family": "Times New Roman"})
    ax.set_ylabel('Size (cm)', fontdict={"family": "Times New Roman"})
    ax.xaxis.set_tick_params(labelsize=8)  # 调整刻度标签的大小
    ax.yaxis.set_tick_params(labelsize=8)

# 调整第一行子图的位置居中显示
plt.subplots_adjust(hspace=0.5, wspace=0.3, top=0.9, bottom=0.1, left=0.1, right=0.9)
plt.tight_layout(rect=[0, 0, 1, 0.95])  # 调整布局使得colorbar不会遮挡标题

# 添加共享的colorbar，使用最后一个子图的imshow来生成colorbar
cbar = fig.colorbar(im4, ax=axs.ravel().tolist(), label=r'$S_{21}$', fraction=0.046, pad=0.04,norm = norm  )

# 显示图形
plt.rc('font', family='Times New Roman', size=12)
# plt.savefig('d:\\MV\\MV 1\\1\\2024-04-20.png')
plt.show()
