# -*- coding: utf-8 -*-
def enhanceresolution(data2d,width,height,title):
    #%% 导入模块 import modules
    import matplotlib.pyplot as plt  
    import numpy as np
    data2d = data2d[::-1]  # 换行  因为 imshow 作图 是从下往上的
    #%% d 转化为 sigma d 为 厘米
    def d_sigma(data2d):   #  data2d是形式参数
        data2d = 0.01 * data2d
        L = 81
        n22 = 1.51; n33 = 1.47;  q66 = -10.26
        beta22 = 1 / n22**2;  beta33 = 1 / n33**2 
        for i in range(0,np.shape(data2d)[0]):
            for j in range(0,np.shape(data2d)[1]):
                data2d[i,j] = (beta33 - beta22) * data2d[i,j] ** 2 / 8 * q66 * L ** 2
        return (data2d) 
    data2d = d_sigma(data2d)
    #%% 矩阵扩充  matrix expand 至少扩充到 100 * 100
    benzhenghangshu = np.shape(data2d)[0]  #行数  
    benzhenglieshu = np.shape(data2d)[1]  #列数
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
    return (data2d)
    #%% 创建画布
    fig, ax = plt.subplots(figsize = (10,10)) #facecolor='#F5F5EB',
    # 创建一个画布，把这个画布赋值给变量fig
    # 同时在这个画布上创建了一个axes，把这个axes赋值给ax
    # 所有未来的fig.xxx都是对这个画布的操作，所有ax.xxx都是对这个axes的操作
    im01 = ax.imshow(data2d,origin='lower',cmap = 'jet')   #          
    
    #%% 坐标轴 标题 图例
    plt.xlabel('Size (cm)')
    plt.ylabel('Size (cm)')
    
    old_ticksx = np.linspace(0,np.shape(data2d)[1],10)
    old_ticksy = np.linspace(0,np.shape(data2d)[0],10)

    new_ticksx = np.linspace(0,width,10)  #  对新的轴设定范围
    new_ticksy = np.linspace(0,height,10)
    new_ticksx = np.round(new_ticksx,1)  #   对新的轴坐标取小数点后一位
    new_ticksy = np.round(new_ticksy,1)
    ax.xaxis.set_ticks(old_ticksx,new_ticksx)
    ax.yaxis.set_ticks(old_ticksy,new_ticksy) 
    
    ax.set_title('S21 of %s KDP'%(title))
    
    fig.colorbar(im, ax=ax, label='S21',fraction=0.046, pad=0.04)  
    # plt.savefig(‘heatmap.svg’) # 保存图片 
    plt.show()
    