import cv2
import pupil_apriltags as apriltag
import numpy as np 


cap = cv2.VideoCapture(0)
detector = apriltag.Detector(families='tag36h11')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    results = detector.detect(img_gray)

    for result in results:
        cv2.circle(frame, (int(result.center[0]), int(result.center[1])), 5, (0, 0, 255), -1)
        cv2.putText(frame, str(result.tag_id), (int(result.center[0]), int(result.center[1])), 1, 1, (0, 255, 255))

        idx = 0
        for corner in result.corners:
            idx += 1
            cv2.circle(frame, (int(corner[0]), int(corner[1])), 5, (0, 0, 255), -1)
            cv2.putText(frame, str(idx), (int(corner[0]), int(corner[1])), 1, 1, (0, 255, 255))
            
            # img = cv2.imread("/Users/bagseonghyeon/Desktop/schoolstudy/opencv/2학기/마커탐지/dora.jpeg", cv2.IMREAD_GRAYSCALE)
            # img = cv2.resize(img, 400,400)
            # h, w = img.shape
            # point1_src = np.float32([[0,0], [w,0], [0,w], [w,h]]) 
            # point1_dst = np.float32([[0,0], [w,0], [0,w], [w,h]]) 
            # per_mat1 = cv2.getPerspectiveTransform(point1_src, point1_dst) 
            # res1 = cv2.warpPerspective(img, per_mat1, (w,h)) 

    cv2.imshow('도라에에에몽', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()