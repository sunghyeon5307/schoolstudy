import cv2

CAMERA_ID = 0

cam = cv2.VideoCapture(CAMERA_ID)
if cam.isOpened() == False:
    print("카메라x")
    exit()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cam.read()
    if not ret:
        print("프레임x")
        break
    
    cv2.imshow('image', frame)
    
    key = cv2.waitKey(5) & 0xFF
    
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows