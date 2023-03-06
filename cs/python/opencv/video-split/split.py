# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:54:11 2023

@author: shiduyule
"""

import cv2
import os

# 读取AVI文件
vidcap = cv2.VideoCapture('f:\\coscopic\\B1\\B1-7.avi')

# 获取总帧数
total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

# 获取帧率
fps = int(vidcap.get(cv2.CAP_PROP_FPS))

# 计算每个间隔多少帧
interval = total_frames // 20

# 创建保存图像的文件夹
if not os.path.exists('video_jpg'):
    os.makedirs('video_jpg')

# 从头到尾每隔相等时间抽取总数20张图像
for i in range(0, total_frames, interval):
    # 读取帧
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, i)
    success, image = vidcap.read()

    # 如果读取成功则保存图像
    if success:
        filename = f"video_jpg/frame_{i}.jpg"
        cv2.imwrite(filename, image)
