import cv2
import numpy as np

# 加载图像
img = cv2.imread('c.bmp', cv2.IMREAD_GRAYSCALE)

# 应用二值化处理
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 寻找图像中的轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 选择最大的轮廓
max_area = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        best_contour = contour

# 拟合椭圆
ellipse = cv2.fitEllipse(best_contour)

# 绘制椭圆并标注两个顶点
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.ellipse(img, ellipse, (0, 255, 0), 2)
(x, y), (a, b), angle = ellipse
cv2.circle(img, (int(x-a/2), int(y)), 5, (0, 0, 255), -1)
cv2.circle(img, (int(x+a/2), int(y)), 5, (0, 0, 255), -1)

# 计算顶点距离
distance = a

# 显示图像并输出距离值
cv2.imshow('image', img)
print('Distance between two vertices: ', distance)

# 等待用户按下任意按键退出程序
cv2.waitKey(0)
cv2.destroyAllWindows()

pixel_to_mm = 16 # 每个像素代表的实际距离（单位：毫米）
distance_in_mm = distance * pixel_to_mm
print('Distance between two vertices (mm): ', distance_in_mm)

