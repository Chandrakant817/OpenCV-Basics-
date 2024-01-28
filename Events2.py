import cv2
import numpy as np

def draw(event,x,y,flag,params):
    if event == 0:
        print("Event trigged")
        #print(event)
    if event == 1:
        print("Mouse Clicked down")
        cv2.circle(img,center=(x,y),radius=50,color=(0,0,255),thickness=-1)

    if event == 4:
        print("Mouse Up Click")


cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)

img = cv2.imread(r"C:\Users\Chandrakant\Desktop\OpenCV\Chandrakant_Thakur.jpg")
#img = np.zeros((512,512,3))
while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cv2.destroyAllWindows()