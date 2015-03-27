""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

cap = cv2.VideoCapture(-1)
face_cascade = cv2.CascadeClassifier('/home/rebecca/Documents/SoftDes/SoftDesSp15/toolbox/image_processing/haarcascade_frontalface_alt.xml')
kernel = np.ones((30,30),'uint8')

while True:
    ret, frame = cap.read() # captures each frame
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize = (20,20))
    for (x,y,w,h) in faces:
        #cv2.rectangle(frame,(x,y), (x+w, y+h), (0,0,255))
        frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
        cv2.circle(frame, (int(x + w/6), int(y + w/3)), int(w/8) , (255, 255, 255), -1)
        cv2.circle(frame, (int(x + 5*w/6), int(y + w/3)), int(w/8), (255, 255, 255), -1)
        cv2.ellipse(frame, (int(x + w/6 - w/16), int(y + w/3)), (int(w/32), int(w/16)), 0, 360, 0, (0, 0, 0), int(w/20))
        cv2.ellipse(frame, (int(x + 5*w/6 + w/16), int(y + w/3)), (int(w/32), int(w/16)), 0, 360, 0, (0, 0, 0), int(w/20))
        cv2.ellipse(frame, (int(x + w/7), int(y + w)), (int(w/8), int(h/4)), 0, 270, 180, (200, 200, 0), int(w/15))
        cv2.ellipse(frame, (int(x + 2*w/7), int(y + w)), (int(w/8), int(h/4)), 0, 250, 160, (200, 200, 0), int(w/15))
        cv2.ellipse(frame, (int(x + 3*w/7), int(y + w)), (int(w/8), int(h/4)), 0, 230, 140, (200, 200, 0), int(w/15))
        cv2.ellipse(frame, (int(x + 4*w/7), int(y + w)), (int(w/8), int(h/4)), 0, -50, 40, (200, 200, 0), int(w/15))
        cv2.ellipse(frame, (int(x + 5*w/7), int(y + w)), (int(w/8), int(h/4)), 0, -70, 20, (200, 200, 0), int(w/15))
        cv2.ellipse(frame, (int(x + 6*w/7), int(y + w)), (int(w/8), int(h/4)), 0, -90, 0, (200, 200, 0), int(w/15))
        cv2.line(frame, (int(x + w/2), int(y + w+ w/6)), (int(x + w/2), int(y + w - w/6)), (200, 200, 0), int(w/15))
    cv2.imshow('frame', frame) #shows the frame
    if cv2.waitKey(1) & 0xFF == ord('q'): #press q to close
        break

cap.release()
cv2. destroyAllWindows
