import cv2
import numpy as np

# 定义滑块回调函数
def update_kernel(x):
    global img, kernel_sharpen_1
    # 根据滑块值更新卷积核
    kernel_sharpen_1 = np.array([
        [-1, -x, -1],
        [-x, 200 + 8 * x, -x],
        [-1, -x, -1]
    ])
    # 应用卷积核
    img_sharpened = cv2.filter2D(img, -1, kernel_sharpen_1)
    # 显示处理后的图像
    cv2.imshow('sharp', img_sharpened)

# 加载图像
img = cv2.imread('image.jpg')

# 初始化卷积核和滑块初始值
kernel_sharpen_1 = np.array([
    [-1, -40, -1],
    [-20, 200, -20],
    [-1, -40, -1]
])
init_trackbar_val = 40

# 创建窗口和滑块
cv2.namedWindow('sharp')
cv2.createTrackbar('Strength', 'sharp', init_trackbar_val, 100, update_kernel)

# 显示原始图像
cv2.imshow('original', img)

# 进入事件循环
while True:
    # 等待按键事件
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # 按下 ESC 键退出
        break

# 释放窗口和摄像头资源
cv2.destroyAllWindows()
