#run code in terminal in vs code\udemy\

import cv2
import sys

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("scc.jpg", cv2.IMREAD_COLOR)

if img is None:
    sys.exit("image couldnt be loaded")
    
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=15)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (100,0,0), 3)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("ass", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()