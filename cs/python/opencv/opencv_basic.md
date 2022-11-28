### 读取图片

```python
import cv2
image = cv2.imread("name_of_image.jpg")
print(image.shape)
```

### 裁剪图片
```python
crop = image[0.4*image.shape[0]:0.6*image.shape[0],0.4*image.shape[1]:0.6*image.shape[1]]

cv2.imshow("crop",crop)
cv2.waitKey()
```