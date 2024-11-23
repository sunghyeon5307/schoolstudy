import cv2
import numpy as np

# camera setting
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)

# q키를 눌러서 순서대로 배경 사진 촬영하기
winName1 = 'background capture'
while cam.isOpened():
    status, frame = cam.read()
    if status:
        cv2.imshow(winName1, frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        break

winName2 = 'foreground capture'
while cam.isOpened():
    status, frame = cam.read()
    if status:
        img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img3 = cv2.absdiff(img1, img2)
        cv2.imshow(winName2, img3)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break