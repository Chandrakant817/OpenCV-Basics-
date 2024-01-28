import cv2
import numpy as np

flag = False
ix = -1
iy = -1

def draw(event,x,y,flags,params):
    
    global flag,ix,iy
    
    if event == 1:
        flag = True
        ix = x
        iy = y

    elif event == 4: 
        fx = x
        fy= y
        flag = False
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color = (0,0,0),thickness=1)

        #Crop tool
        croped = img[iy:fy,ix:fx] #Height #width
        cv2.imshow("window",croped)
        cv2.waitKey(0)


cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw) 

## Image
img = cv2.imread(r"C:\Users\Chandrakant\Desktop\OpenCV\Chandrakant_Thakur.jpg")

while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break
cv2.destroyAllWindows()