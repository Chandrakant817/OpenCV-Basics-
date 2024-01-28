import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    #cvt BGR to GRAY scale video
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2LUV)
    #img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    cv2.imshow("window",img_gray)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cv2.destroyAllWindows()