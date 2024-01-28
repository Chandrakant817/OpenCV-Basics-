import cv2
import numpy as np

#img = cv2.imread(r"C:\Users\Chandrakant\Desktop\OpenCV\Chandrakant_Thakur.jpg")
img = np.zeros((512,512,3))

while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cv2.destroyAllWindows()

