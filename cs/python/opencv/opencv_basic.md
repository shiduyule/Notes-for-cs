### cv2.imread() 读取图片
```python
import cv2
image = cv2.imread("name_of_image.jpg")
print(image.shape)
```

### convert colours
```python
image = image[:,:, ::-1]
```

### image[:,:] 裁剪图片
```python
crop = image[0.4*image.shape[0]:0.6*image.shape[0],0.4*image.shape[1]:0.6*image.shape[1]]

cv2.imshow("crop",crop)
cv2.waitKey()
```

### recongnize circle  
```python
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread("000.jpeg",0)

#image = image[:,:, ::-1]
#img = image[int(0.4*image.shape[0]):int(0.7*image.shape[0]),int(0.35*image.shape[1]):int(0.55*image.shape[1])]

img = cv.medianBlur(img,5) 
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=500,maxRadius=600)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
plt.imshow(cimg)
# image = image[:,:, ::-1]
plt.figure()
```