# -*- coding: utf-8 -*-
"""
Created on Thu May 23 08:45:24 2024

@author: shiduyule
"""

def changexy(data2d):
    import matplotlib.pyplot as plt  
    import numpy as np
    
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
    return(data2d)  