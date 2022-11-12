## 数组维度  和variable窗口的size不一样
```python 
Numpy.array 同质运算方便  list中不同质  
维度的判定是中括号的层数

0. 0D
a = np.array(1)  # 圆括号内部是a的真实值 array = 数组
a = [1]  

1. 1D
a = np.array([1,2,3]) 
a.ndim  　#　数组维度  

2. 2D 
a = np.array([
    [12,3,5,7],
    [11,2,4,6],
    [10,8,6,7]]) 

3. 3D 
a = np.array([
       [[ 1,  2,  3],
        [ 4,  5,  6],
        [ 7,  8,  9]],

       [[10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]],

       [[19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]]])
```
## numpy 生成指定范围内的一组有序的一维数组
```python
t = np.linspace(0, 2 * np.pi, 1024)
t = np.linspace(起始值，结束值包括，采样数目)
t = np.arange(起始值，结束不包括，步长默认为1)
```

## 数组 升维度
```python
x[:, np.newaxis]  放在后面，会给列上增加维度
x[np.newaxis, :]  放在前面，会给行上增加维度

data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
data
```
## 数组 合并
```python
1. array2D = np.array([data1,data2])
