import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Chandrakant\Desktop\OpenCV\Chandrakant_Thakur.jpg")


img_crop = img[0:300,0:300]

cv2.imwrite("Save Image Experiment.jpg",img_crop)