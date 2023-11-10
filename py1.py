

import cv2
import serial 
import numpy as np

def set_res(cap, x,y):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(x))
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(y))

ser = serial.Serial('COM3', 250000)  

cap = cv2.VideoCapture(1)

frame_w = 640
frame_h = 480
set_res(cap, frame_w,frame_h)

# Create the haar cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while(True):
    ret, frame = cap.read()
    cap.read()
    
    frame=cv2.flip(frame,1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = np.array([]) 
    faces = face_cascade.detectMultiScale( gray,1.1,4)
    

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    if ([i for i in faces]):                                     
        face_center_x = faces[0,0]+faces[0,2]/2
        face_center_y = faces[0,1]+faces[0,3]/2
        #print(faces)
        err_x = 30*(face_center_x - frame_w/2)/(frame_w/2)
        err_y = 30*(face_center_y - frame_h/2)/(frame_h/2)
        ser.write((str(err_x) + "x!").encode())        
        ser.write((str(err_y) + "y!").encode())        
        print("X: ",err_x," ","Y: ",err_y)
    else:
        ser.write("o!".encode())  
              
                     
ser.close()
cap.release()
cv2.destroyAllWindows()
