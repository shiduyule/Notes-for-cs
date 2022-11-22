### 面向对象的语法
![](images/2022-11-22-10-19-49.png)

```python
import matplotlib.pyplot as plt
import numpy as np
A = np.arange(1,5)
B = A**2
C = A**3
```

```python
fig, ax = plt.subplots(figsize=(14,7))  
# fig, ax = plt.subplots(2,1,figsize(14,7))
# ax[0].***
# ax[1].***
```
### 创建画布
```python

创建一个大小为（14，7）的画布，把这个画布赋值给变量fig

同时在这个画布上创建了一个axes，把这个axes赋值给ax

所有未来的fig.xxx都是对这个画布的操作，所有ax.xxx都是对这个axes的操作

如果你有两个图，那么ax是一个有两个元素ax[0],ax[1] 的list
ax[0]就对应第一个subplot的ax
```
### 作图
```python
ax.plot(A,B)
ax.plot(B,A)
```

