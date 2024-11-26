import cv2
import sys
import pupil_apriltags as apriltag
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Camera open failed!')
    sys.exit()

# 탐지를 위한 detector 생성
detector = apriltag.Detector(families='tag36h11')

# 삽입할 이미지를 불러오기 (dora.jpeg)
insert_img = cv2.imread('/Users/bagseonghyeon/Desktop/schoolstudy/opencv/2학기/마커탐지/dora.jpeg')

# 불러온 이미지의 크기 추출
h, w, _ = insert_img.shape

while True:
    # 카메라로부터 영상 읽기
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (960, 540))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 영상에서 AprilTag 찾기
    results = detector.detect(img_gray)

    # 찾은 AprilTag를 하나하나 확인 및 표시하기
    for result in results:
        print(result.tag_id, ':', result.center[0], ',', result.center[1])
        cv2.circle(img, (int(result.center[0]), int(result.center[1])), 5, (0, 0, 255), -1)
        cv2.putText(img, str(result.tag_id), (int(result.center[0]), int(result.center[1])), 1, 1, (0, 255, 255))

        # Tag의 모서리 좌표 가져오기
        corners = result.corners
        for idx, corner in enumerate(corners):
            cv2.circle(img, (int(corner[0]), int(corner[1])), 5, (0, 0, 255), -1)
            cv2.putText(img, str((idx+1) % 4 + 1), (int(corner[0]), int(corner[1])), 1, 1, (0, 255, 255))

        # 원본 이미지의 코너점 (삽입할 dora 이미지의 코너)
        pts_src = np.array([[0, h-1], [w-1, h-1], [w-1, 0], [0, 0]], dtype='float32')
        # pts_src = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], dtype='float32')
        
        # 검출된 AprilTag의 코너점 (대상 영상의 코너)
        pts_dst = np.array(corners, dtype='float32')

        # 변환 행렬 계산
        M = cv2.getPerspectiveTransform(pts_src, pts_dst)

        # 원본 이미지를 대상 영상의 태그 영역에 맞게 변환
        warped_img = cv2.warpPerspective(insert_img, M, (img.shape[1], img.shape[0]))

        # 태그 영역에 삽입된 이미지를 덮어쓰기
        mask = np.zeros_like(img, dtype=np.uint8)
        cv2.fillConvexPoly(mask, pts_dst.astype(int), (255, 255, 255))
        img = cv2.bitwise_and(img, cv2.bitwise_not(mask))
        img = cv2.bitwise_or(img, warped_img)

    # 최종적으로 표시된 결과 출력하기
    cv2.imshow('test', img)
    key = cv2.waitKey(33)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
