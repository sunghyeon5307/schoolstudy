import cv2
import os

cap = cv2.VideoCapture('/Users/bagseonghyeon/Desktop/schoolstudy/opencv/2학기/images/video7.mp4')

while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('image', frame)
        
        key = cv2.waitKey(30) & 0xFF

        if key == ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
