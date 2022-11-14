## 数组维度  (和variable窗口的size不一样)
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

## numpy 数组的索引
```python
data2d[a,b] = 左闭右开
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
```

## 数组整体计算
```python
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
```

```python
1. 获取数组的大小
data2dshape = np.shape (data2d) 这是一个元组
i = data2dshape[1]   索引
j = data2dshape[2]

```


```python
随机生成数组
data2d = np.random.random((1000,1000))
```

```python
a = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
b = np.array([2,5,8])
# 2代表下标，这里代表插入到第三列，axis=1，插入一列，axis=0，插入一行
a =np.insert(a, 2, b, axis=1)

#插入多列
c = np.array([[1,4,7],[2,5,8]]).T
np.insert(a, [0,1], c, axis=1)
 
输出：
[[1 2 2 3]
 [4 5 5 6]
 [7 8 8 9]]
 
[[1 1 2 2 3]
 [4 4 5 5 6]
 [7 7 8 8 9]]

```

```python
 x = np.empty([3,2], dtype = int) 
```


```python
数组转置
t6 = t5.transpose()
```