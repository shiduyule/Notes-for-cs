import cv2
import numpy as np

# 读取图像
img = cv2.imread('Cr1j8.bmp')

# 图像平滑处理
img = cv2.medianBlur(img, 5)

# 转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化处理
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# 形态学操作
kernel = np.ones((5,5), np.uint8)
thresh = cv2.erode(thresh, kernel, iterations=1)
thresh = cv2.dilate(thresh, kernel, iterations=1)

# 应用Canny边缘检测算法
edges = cv2.Canny(thresh, 50, 150)

# 使用霍夫变换找到曲线参数并提取顶点
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=30, maxLineGap=10)
points = []
for line in lines:
    x1, y1, x2, y2 = line[0]
    points.append((x1, y1))
    points.append((x2, y2))

# 计算顶点之间的距离
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        dist = np.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
        distances.append(dist)

# 输出距离的平均值
print('Mean distance between vertices:', np.mean(distances))