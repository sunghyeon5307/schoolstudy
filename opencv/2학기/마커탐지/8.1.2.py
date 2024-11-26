import cv2
import pupil_apriltags as apriltag

# 사진 불러오기
img = cv2.imread('/Users/bagseonghyeon/Desktop/schoolstudy/opencv/2학기/마커탐지/aprilImage.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 탐지를 위한 detector 생성
# detector = apriltag.Detector()
detector = apriltag.Detector(families='tag36h11')

#영상에서 aprilTag 찾기
results = detector.detect(img_gray)

# 찾은 aprilTag를 하나하나 확인 및 표시하기
for result in results:
    print(result.tag_id, ':', result.center[0], ',', result.center[1])
    cv2.circle(img, (int(result.center[0]), int(result.center[1])), 5, (0, 0, 255), -1)
    cv2.putText(img, str(result.tag_id), (int(result.center[0]), int(result.center[1])), 1, 1, (0, 255, 255))

    # Tag의 모서리를 표시하기 위한 for loop
    idx = 0
    for corner in result.corners:
        idx = idx + 1
        cv2.circle(img, (int(corner[0]), int(corner[1])), 5, (0, 0, 255), -1)
        cv2.putText(img, str(idx), (int(corner[0]), int(corner[1])), 1, 1, (0, 255, 255))

# 최종적으로 표시된 결과 확인하기
cv2.imshow('test', img)
cv2.waitKey(0)
