# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 09:14:50 2023

@author: shiduyule
"""

import cv2
import math

# 鼠标事件的回调函数
def mouse_callback(event, x, y, flags, params):
    # 左键单击，记录坐标并绘制圆圈
    if event == cv2.EVENT_LBUTTONDOWN:
        global click_count, pt1, pt2, img_copy
        if click_count == 0:
            pt1 = (x, y)
        elif click_count == 1:
            pt2 = (x, y)
            # 计算距离并在图像上绘制线段
            dist = math.sqrt((pt2[0] - pt1[0])**2 + (pt2[1] - pt1[1])**2)
            cv2.line(img_copy, pt1, pt2, (0, 0, 255), 2)
            cv2.putText(img_copy, "{:.2f}px".format(dist), (int((pt1[0] + pt2[0]) / 2), int((pt1[1] + pt2[1]) / 2)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.imshow('image', img_copy)
            click_count = -1
        click_count += 1


# 读入图像
img = cv2.imread('c.bmp')

# 复制一份图像并注册鼠标事件回调函数
img_copy = img.copy()
click_count = 0
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

# 显示图像并等待鼠标事件
cv2.imshow('image', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

##############           1cm    =====      160 px
