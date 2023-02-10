# -*- coding: utf-8 -*-
def enhanceresolution(data2d,width,height,title):
    #%% 导入模块 import modules
    import matplotlib.pyplot as plt  
    import numpy as np
    from numpy import mean, sqrt, square
    data2d = data2d[::-1]  # 考虑到 imshow 函数的 从下往上画 
    #%% 矩阵输入 matrix input
    # =============================================================================
    # 利用numpy中的二维数组作为容器  首先手动输入光轴倾角的数据  10 * 10 
    # =============================================================================
    # data2d = np.array([
        
    # [-1,  -0.8, -0.1,  0.2,  1.1,  1.2,  1.1,  0.2, -0.9 ],
    # [-0.3, 0.1,  0.1, -0.1,  0.5, 1.25, 1.15, 0.25,  0.1],
    # [-0.2,-0.1,  0.1,    0,  1.0,  1.5,  0.2,  0.3,  0.4],
    # [0.2, -0.1,  1.1,  0.2, -0.1,  0.0,  1.1,  1.2,  0.0], 
    # [0.3,  0.4,  0.1, -0.7,  0.2,  0.1,  0.2, -0.1,  0.2],
    # [0.2,  0.8,  0.5, -0.3, -0.1,  0.7,  0.0, -0.2,  0.0],
    # [0.8,  1.1,  0.9,  1.2,  0.2, -0.2, -0.1,  0.0,  0.0],
    # [-0.7, 0.4,  0.5,  0.9,  1.2,  0.0,  0.0,  1.0,  0.0],
    # [-0.9, 0.2,  0.3,  0.4,  1.3,  0.1, -0.2,  0.7,  0.6]  ])
    
    
    
    #%% 矩阵转化 利用matlab中 拟合得到的函数
    def function_distance_theta(x):   # x 是形式参数 data2d是实际参数
        y = 81
        theta = np.arctan(x/y)
        degree = np.degrees(theta)  # 弧度制转角度制
        return (degree)
        
    def function_theta_strain(data2d):
        a0 =   7.363e-05 
        a1 =  -8.187e-05 
        b1 =  -2.305e-05 
        a2 =   7.352e-06 
        b2 =   1.373e-05 
        a3 =   9.547e-07 
        b3 =  -1.768e-06 
        w =       1.798  

        for i in range(0,np.shape(data2d)[0]):
            for j in range(0,np.shape(data2d)[1]):
                x = data2d[i,j]
                if x >= 0:
                    fitfunction =  a0 + a1 * np.cos(x*w) + b1 * np.sin(x*w) + a2 * np.cos(2*x*w) + b2 * np.sin(2*x*w) + a3 * np.cos(3*x*w) + b3 * np.sin(3*x*w)
                    data2d[i,j] = fitfunction
                else:
                    x = -1 * x
                    fitfunction =  a0 + a1 * np.cos(x*w) + b1 * np.sin(x*w) + a2 * np.cos(2*x*w) + b2 * np.sin(2*x*w) + a3 * np.cos(3*x*w) + b3 * np.sin(3*x*w)
                    data2d[i,j] = 1 * fitfunction    # 区分左旋 右旋的时候加上负号 算平均值的时候不加负号 同时导致了正负不分中间的零点被忽略
        return (data2d)
    data2d = function_distance_theta(data2d)
    data2d = function_theta_strain(data2d)
    print(title)
    print('rms = %e'%sqrt(mean(square(data2d))))
    print('avg = %e'%mean(data2d))
    
    #%% 矩阵扩充  matrix expand 至少扩充到 100 * 100
    benzhenghangshu = np.shape(data2d)[0]  #行数  
    benzhenglieshu = np.shape(data2d)[1]  #列数
    #=============================================================================
    #%%扩充列数  设置density 即可
    j = 0
    density = 100  # 插入的矩阵行数为data2d的行数  列数为设置的密度值
    while True: 
        insertcolumn = np.empty([np.shape(data2d)[0] ,density], dtype = float)
        i = 0
        while i < np.shape(data2d)[0]:  # 当行数在总行数范围内
            insertcolumn[i,:] = np.linspace(data2d[i,j],data2d[i,j+1],density+1,endpoint = False)[1:density+1] # 以第i行第j列 和第i行第j+1列为起始值   这里是 5行 10列数组   ## 注意数组 索引的左闭右开 
            i = i + 1 
            # print(j,i)
            # print('\n')    
        insertcolumn = insertcolumn.transpose()
        data2d = np.insert(data2d, j+1,insertcolumn, axis=1) # 插入density列
        j = j + 1 + density 
        muqianlieshu = np.shape(data2d)[1]
        if muqianlieshu >= ((benzhenglieshu-1)*density + benzhenglieshu):
            break
    #============================================================================
    #%%扩充行数
    i = 0
    # 插入的矩阵行数为data2d的行数  列数为设置的密度值
    density = int((height * density)/width)
    while True:
        insertline = np.empty([density,np.shape(data2d)[1]], dtype = float)
        j = 0   # 从第1列开始
        while j < np.shape(data2d)[1] :  # 当列数在总列数范围内
            insertline[:,j] = np.linspace(data2d[i,j],data2d[i+1,j],density+1,endpoint = False)[1:density+1]  # 将第i行和第i加一行的中间值赋给insertline的第j列
            j = j + 1 
            
        data2d = np.insert(data2d, i+1,insertline, axis=0) # 插入多行
        i = i + 1 + density 
        muqianhangshu = np.shape(data2d)[0]  # 目前行数
        if muqianhangshu == (benzhenghangshu-1)*density + benzhenghangshu:
            break
    
    #%% 创建画布
    fig, ax = plt.subplots(figsize = (5.4,4),dpi = 600)#facecolor='#F5F5EB',
      
    # 创建一个画布，把这个画布赋值给变量fig
    
    # 同时在这个画布上创建了一个axes，把这个axes赋值给ax
    
    # 所有未来的fig.xxx都是对这个画布的操作，所有ax.xxx都是对这个axes的操作
    im = ax.imshow(data2d,origin='lower',cmap = 'jet')   #          
    
    #%% 坐标轴 标题 图例
    plt.xlabel('Size (cm)',fontdict={"family": "Times New Roman"})
    plt.ylabel('Size (cm)',fontdict={"family": "Times New Roman"})
    
    old_ticksx = np.linspace(0,np.shape(data2d)[1],10)
    old_ticksy = np.linspace(0,np.shape(data2d)[0],10)

    new_ticksx = np.linspace(0,width,10)  #  对新的轴设定范围
    new_ticksy = np.linspace(0,height,10)
    new_ticksx = np.round(new_ticksx,1)  #   对新的轴坐标取小数点后一位
    new_ticksy = np.round(new_ticksy,1)
    ax.xaxis.set_ticks(old_ticksx,new_ticksx)
    ax.yaxis.set_ticks(old_ticksy,new_ticksy) 
    
    ax.set_title('shear stress of %s sample   '%(title))
    
    fig.colorbar(im, ax=ax, label=r'$\sigma_{21}$',fraction=0.046, pad=0.04)  
    plt.savefig('F:\----KDP-Data----\shear stress\%s.png'%(title)) # 保存图片 
    plt.rc('font', family='Times New Roman', size=13)
    plt.show()
    return (data2d)
    # A1 4cm 3.5cm
# A2 3.8cm  4.2cm
# A3  4cm   4cm
# A4  4.5cm  4.4cm
# A5  4.4cm  3.8cm
# A6  4.6cm  4.3cm

# σ = 0.08 

# 先按照晶体记号笔标记的来
# B1 4.8 4.2   Cr:10 ppm
# B2 4.3 4.4   Cr:20 ppm
# B3 4.5 4.5   Cr:30 ppm
# B4 4.05 4.2  Cr:40 ppm
# B5 4.2 3.8   Cr:5 ppm   边角 ： D 1

# B0 4.5 4.5 Cr:10ppm
# B6 4.6 4.5 Cr:50ppm

# C3  6.3cm  4cm
# 有裂纹的晶体结构应力  待测