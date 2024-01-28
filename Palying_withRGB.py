import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Chandrakant\Desktop\OpenCV\Chandrakant_Thakur.jpg")

#img[:,:,0] = 0
#img[:,:,1] = 0
#img[:,:,2] = 0

imgblue = img[:,:,0]
imggreen = img[:,:,1]
imgred = img[:,:,2]

img_hstack = np.hstack((imgblue,imggreen,imgred))
cv2.imshow("window",img_hstack)
cv2.waitKey(0)