import os
import cv2 as cv

cap=cv.VideoCapture('test.mp4')

while cap.isOpened():
    success, frame=cap.read()
    if success:
        cv.imshow('image', frame)

        key=cv.waitKey(30) & 0xFF

        # 시간을 늦추면 어떻게 될까?
        # key = cv.waitKey(100) & 0xFF
        if(key==27):
            break
    else:
        break

cap.release()

# 창 닫고 끝
cv.destroyAllWindows()