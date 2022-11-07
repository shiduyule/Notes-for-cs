"""
========================================
Interactive Adjustment of Colormap Range
========================================

Demonstration of how a colorbar can be used to interactively adjust the
range of colormapping on an image. To use the interactive feature, you must
be in either zoom mode (magnifying glass toolbar button) or
pan mode (4-way arrow toolbar button) and click inside the colorbar.

When zooming, the bounding box of the zoom region defines the new vmin and
vmax of the norm. Zooming using the right mouse button will expand the
vmin and vmax proportionally to the selected region, in the same manner that
one can zoom out on an axis. When panning, the vmin and vmax of the norm are
both shifted according to the direction of movement. The
Home/Back/Forward buttons can also be used to get back to a previous state.

.. redirect-from:: /gallery/userdemo/colormap_interactive_adjustment
"""
import matplotlib.pyplot as plt  
import numpy as np

t = np.linspace(0, 2 * np.pi, 1024)  # t的取值范围是(0,2π) 像素点是1024
b = np.sin(t)[:, np.newaxis]
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :] # 矩阵化

# =============================================================================
# print("数据np.sin(t)一个%d维的数组"%np.sin(t).ndim)
# print(np.sin(t))
# print('\n')
# print("数据np.sin(t)[:, np.newaxis]是一个%d维的数组"%np.sin(t)[:, np.newaxis].ndim)   
# print(np.sin(t)[:, np.newaxis])
# print('\n')
# print("数据data2d是一个%d维的数组"%data2d.ndim) 
# print(data2d)  
# =============================================================================

#%% 创建画布
fig, ax = plt.subplots(facecolor='#F5F5EB')  # 等价于 plt.subplots(1,1) 创建画布fig 和一个子区域
im = ax.imshow(data2d,)          
ax.set_title('Pan on the colorbar to shift the color mapping\n'
             'Zoom on the colorbar to scale the color mapping')

fig.colorbar(im, ax=ax, label='Interactive colorbar')  

plt.show()
