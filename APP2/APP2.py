#motion detector


import cv2
import time
import sys

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)      #starting webcam

video.read()     # read one frame, discard it 
time.sleep(1)    # hide our face+hand fully out of view, until this completes


if not video.isOpened():                        #checking whether the webcam is working
    print("cannot open camera")
    exit()


first_frame=None                                #first frame variale

while True:
   
    check, frame = video.read()

    if not check:
        print("cant receive frames. Exiting......")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)          #converting frames to grayscale
    gray = cv2.GaussianBlur(gray, (21, 21), 0)              #applying gaussian blurr, parameter2 - dimensions of blurr
    
    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)                                        #getting difference of first frame and the consecutive frames
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]         #pixels with value<30 are to be colored white(255)
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)                   #applying smoothening effect for 2 iterations

    (contrs, _) = cv2.findContours(threshold_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)     #finding contours around white pixels, findContours() returns tuple

    for contours in contrs:
        if cv2.contourArea(contours) < 500:                                            
            continue
        else:
            (x,y,h,w) = cv2.boundingRect(contours)                                      #drawing rec around contours with area>1000
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
   
    cv2.imshow("delta", delta_frame)
    cv2.imshow("color", frame)
    cv2.imshow("thresh", threshold_frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break


video.release()
cv2.destroyAllWindows()
"""

#motion detector with start and end timestamps

import cv2
import time
import sys
from datetime import datetime
import pandas

data = pandas.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not video.isOpened():
    print("cannot open camera")
    exit()


first_frame=None
status = 0
status_ls = [None, None]
time = []

while True:
   
    check, frame = video.read()

    status = 0
    status_ls.append(status)

    if not check:
        print("cant receive frames. Exiting......")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=5)

    (contrs, _) = cv2.findContours(threshold_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contours in contrs:
        if cv2.contourArea(contours) < 1000:
            continue
        else:
            status = 1
            
            (x,y,h,w) = cv2.boundingRect(contours)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)

    status_ls.append(status)    
   
    if status_ls[-1]==1 and status_ls[-2]==0:
        time.append(datetime.now())
    if status_ls[-1]==0 and status_ls[-2]==1:
        time.append(datetime.now())
    
    cv2.imshow("delta", delta_frame)
    cv2.imshow("color", frame)
    cv2.imshow("thresh", threshold_frame)

    key=cv2.waitKey(1)
    if key==ord('q'):
        if status==-1:
            time.append(datetime.now())
        break

#print(status_ls)
#print(time)

for i in range(0, len(time), 2):
    data = data.append({"Start":time[i], "End":time[i+1]}, ignore_index=True)

#data.to_csv("Timestamps.csv")

video.release()
cv2.destroyAllWindows()

"""