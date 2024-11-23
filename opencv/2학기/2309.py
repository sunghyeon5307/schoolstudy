import cv2

def nothing():
    pass

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.createTrackbar('mode', 'img', 0, 1, nothing)
cv2.createTrackbar('history', 'img', 0, 500, nothing)

cv2.setTrackbarPos('mode', 'img', 0)
cv2.setTrackbarPos('history', 'img', 500)

bgMethod1 = cv2.createBackgroundSubtractorMOG2()
bgMethod2 = cv2.createBackgroundSubtractorKNN()

x = 100

bgMethod1.setHistory(x)
bgMethod1.setVarThreshold(x)

CAMERA_ID = 0

cam = cv2.VideoCapture(CAMERA_ID)
if not cam.isOpened():
    print("카메라x")
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        print("프레임x")
        break
    
    cv2.imshow('img', frame)
    
    key = cv2.waitKey(5) & 0xFF
    
    if key == 27:  
        break

cam.release()
cv2.destroyAllWindows()  