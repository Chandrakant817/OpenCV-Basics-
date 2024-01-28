import cv2
import numpy as np

#img = cv2.imread(r"C:\Users\Chandrakant\Desktop\OpenCV\Chandrakant_Thakur.jpg")
img = np.zeros((512,512,3))

#Create a Rectange
cv2.rectangle(img, pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=3)

# Create a Circle
cv2.circle(img,center=(100,400),radius=50,color=(0,0,255),thickness=3)

# Create a Line
cv2.line(img,pt1=(0,0),pt2=(512,512),color=(0,255,0),thickness=3)

# Create a Text
cv2.putText(img,text="Hello Chandrakant",org=(75,75),fontScale=4,fontFace=cv2.FONT_ITALIC,
            color=(0,255,255),thickness=1,lineType=cv2.LINE_AA)

cv2.imshow("window",img)
cv2.waitKey(0)