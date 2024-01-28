import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Chandrakant\Desktop\OpenCV\Chandrakant_Thakur.jpg")

img_resize = cv2.resize(img,(256,256))
#img_resize1 = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2)) ## Half the Image from original image

cv2.imshow("window",img_resize)
cv2.waitKey(0)