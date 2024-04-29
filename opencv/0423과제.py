import cv2

cam = cv2.VideoCapture(0)
if cam.isOpened() == False:
    print('error')
    exit()
    
while True:
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    key = cv2.waitKey(33)

    if key == ord('a'):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray frame', gray_frame)
        
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
