import cv2
capture = cv2.VideoCapture('stressadd.mp4')
frames, image = capture.read()
count = 0 # counting frames
k=2 # read every k frames
while frames:
  capture.set(cv2.CAP_PROP_POS_MSEC, (count * k))
  cv2.imwrite("frames/frame%d.jpg" % count, image)
  frames,image = capture.read()
  print ('Read frame number: ', count)
  count += 1


