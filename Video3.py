import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))

while True:
    ret,frame = cap.read()
    out.write(frame)

    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("window",img_gray)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cv2.destroyAllWindows() 