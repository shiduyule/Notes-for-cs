
import cv2
import matplotlib.pyplot as plt
image = cv2.imread("c:/Users/shiduyule/Desktop/cv1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 2000, 0.0001, 0.01)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (int(x), int(y)), 1, (0, 0, 210), -1)

image = image[:,:, ::-1]
plt.imshow(image)
plt.show()
#cv2.imshow("corners", image)
#cv2.waitKey()

