import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Chandrakant\Desktop\OpenCV\Chandrakant_Thakur.jpg")

img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("hi",img_grey)
cv2.waitKey(0)
