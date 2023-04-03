import cv2
import numpy as np
import matplotlib.pyplot as plt
# 加载图像
img = cv2.imread('1.jpg')

# 锐化处理
kernel_sharpen_1 = np.array([
    [-1,-40,-1],
    [-40,170,-40],
    [-1,-40,-1]
])
img = cv2.filter2D(img, -1, kernel_sharpen_1)
plt.imshow(img)  #  interpolation='nearest'
plt.show()
#cv2.waitKey(0)

# 预处理图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 自适应阈值二值化处理
# thresh = cv2.adaptiveThreshold(blur, 255, 100, cv2.THRESH_BINARY, 11, 2)
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 131, 3)

# 形态学操作，去除噪点和填充双曲线内部空洞
kernel = np.ones((5, 5), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)

# 通过连通组件分析保留最粗的两条线条
connectivity = 8
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(morph, connectivity, cv2.CV_32S)

# 寻找最长的两条线条
max_lengths = [-1, -1]
max_labels = [-1, -1]
for i in range(1, num_labels):
    length = stats[i, cv2.CC_STAT_WIDTH]
    if length > max_lengths[0]:
        max_lengths[0] = length
        max_labels[0] = i
    elif length > max_lengths[1]:
        max_lengths[1] = length
        max_labels[1] = i

# 保留最粗的两条线条并去除断断续续的点
mask = np.zeros(morph.shape, dtype=np.uint8)
for label in max_labels:
    if label != -1:
        mask[labels == label] = 255
morph = cv2.bitwise_and(morph, morph, mask=mask)

# 展示预处理结果
plt.imshow(morph)
#cv2.waitKey(0)

# 进行霍夫变换，得到累加器数组
accumulator = cv2.HoughLinesP(morph, rho=1, theta=np.pi/180, threshold=50, minLineLength=100, maxLineGap=50)

# 根据双曲线参数绘制双曲线
if accumulator is not None and len(accumulator) == 2:
    for line in accumulator:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 显示结果
plt.imshow(img)
#  cv2.waitKey(0)
#  cv2.destroyAllWindows()
