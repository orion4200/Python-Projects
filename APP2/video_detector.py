import cv2
import time
import sys

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not video.isOpened():
    print("cannot open camera")
    exit()

a=0
start = time.time()
while True:
    a=a+1
    check, frame = video.read()

    if not check:
        print("cant receive frames. Exiting......")
        break

    cv2.imshow("winname", frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

end = time.time()

print(a)
print(end-start)
print(a/(end-start)," fps")

video.release()
cv2.destroyAllWindows()

