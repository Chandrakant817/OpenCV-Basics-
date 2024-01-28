import cv2
import numpy as np
import time

cap = cv2.VideoCapture(r"C:\Users\Chandrakant\Desktop\OpenCV\output.avi")

while True:
    ret,frame = cap.read()

    time.sleep(1/20)
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("window",img_gray)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cv2.destroyAllWindows() 