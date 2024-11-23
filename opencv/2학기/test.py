import cv2
CAMERA_ID = 0
cam = cv2.VideoCapture(CAMERA_ID)

if cam.isOpened() == False:
    print('Can\'t open the CAM(%d)' % (CAMERA_ID))
    exit()

vod = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 30, (1920,1080))

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cam.read()
    if ret == False:
        print("프레임을 얻을 수 없습니다")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', gray)
    
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    vod.write(gray_bgr)
    
    key = cv2.waitKey(50) & 0xFF
    
    if key == 27:
        break
    
cam.release()
vod.release()
cv2.destroyAllWindows()