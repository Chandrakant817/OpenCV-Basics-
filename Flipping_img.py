import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Chandrakant\Desktop\OpenCV\Chandrakant_Thakur.jpg")

img_flip = cv2.flip(img,0) 
#img_flip = cv2.flip(img,1)
#img_flip = cv2.flip(img,-1)

cv2.imshow("window",img_flip)
cv2.waitKey(0)


