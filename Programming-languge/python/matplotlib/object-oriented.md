### 面向对象的语法
![](images/2022-11-22-10-19-49.png)

```python
import matplotlib.pyplot as plt
import numpy as np
A = np.arange(1,5)
B = A**2
C = A**3
```
### 创建画布
```python
fig, ax = plt.subplots(figsize=(14,7))  
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None) 
## 调整子图在画布中的尺寸  left bottom right top 范围[0,1] wspace,hspace 水平和垂直方向上的间距 取值可以大于1

# fig, ax = plt.subplots(2,1,figsize(14,7))
# ax[0].***
# ax[1].***
```

```python

创建一个大小为（14，7）的画布，把这个画布赋值给变量fig

同时在这个画布上创建了一个axes，把这个axes赋值给ax

所有未来的fig.xxx都是对这个画布的操作，所有ax.xxx都是对这个axes的操作

如果你有两个图，那么ax是一个有两个元素ax[0],ax[1] 的list
ax[0]就对应第一个subplot的ax
```
### 作图
```python
ax.plot(A,B) 折线图
x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(15, 15), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend();  # Add a legend.


ax.imshow(data2d) 2D 图片/分布图

```

### axes 
```python
ax.set_title('title context') 
标题
ax.set_xlabel('xlabel', fontsize=18,fontfamily = 'sans-serif',
fontstyle='italic')
x 轴标签
ax.set_ylabel('ylabel', fontsize='x-large',fontstyle='oblique')
y 轴标签
ax.legend()
图例
```

### axis 更换坐标轴范围 finished
```python
ax.xaxis.set_tick_params(rotation=45,labelsize=18,colors='w') 

start, end = ax.get_xlim() 

ax.xaxis.set_ticks(np.arange(start, end,1)) 

ax.yaxis.tick_right()

```

### plt.figsave() 图片保存
```
plt.savefig(heatmap.svg)
```


###  局部放大  太复杂 不适合
```python
https://matplotlib.org/stable/tutorials/toolkits/axes_grid.html
```