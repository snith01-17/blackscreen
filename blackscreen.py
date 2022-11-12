import cv2
import time
import numpy as np

#fourcc is a 4 byte used to specify the video codec algorithm
cap = cv2.VideoCapture(0)

#2 milliseconds
time.sleep(2)

bg = 0

#capturing the background for 60 frames
for i in range(60):
    ret, bg = cap.read()

#flipping the background
bg = np.flip(bg,axis=1)

while True: 
  
    ret, frame = cap.read() 
    print(frame)
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
  
  
    u_black = np.array([104, 153, 70]) 
    l_black = np.array([30, 30, 0]) 
  
    mask = cv2.inRange(frame, l_black, u_black) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  
    f = frame - res 
    f = np.where(f == 0, image, f) 
  
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
  
cap.release() 
cv2.destroyAllWindows() 