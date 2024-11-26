import cv2
import sys
import pupil_apriltags as apriltag
import numpy as np

# 카메라 열기
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Camera open failed!')
    sys.exit()

# 탐지를 위한 detector 생성
detector = apriltag.Detector(families='tag36h11')

# 동영상 열기
vi = cv2.VideoCapture('images/video7.mp4')
if not vi.isOpened():
    print('Video open failed!')
    sys.exit()

while True:
    # 카메라로부터 영상 읽기
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.resize(img, (960, 540))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 동영상 프레임 읽기
    ret_vi, frame = vi.read()
    if not ret_vi:  # 동영상 끝에 도달했으면 다시 시작
        vi.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret_vi, frame = vi.read()

    h, w, _ = frame.shape  # 동영상 프레임의 크기 추출

    # 영상에서 AprilTag 찾기
    results = detector.detect(img_gray)

    # 찾은 AprilTag 처리
    for result in results:
        print(result.tag_id, ':', result.center[0], ',', result.center[1])
        cv2.circle(img, (int(result.center[0]), int(result.center[1])), 5, (0, 0, 255), -1)
        cv2.putText(img, str(result.tag_id), (int(result.center[0]), int(result.center[1])), 1, 1, (0, 255, 255))

        # AprilTag의 모서리 좌표 가져오기
        corners = result.corners
        pts_src = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], dtype='float32')  # 동영상 프레임 코너
        pts_dst = np.array(corners, dtype='float32')  # 태그의 모서리 좌표

        # 변환 행렬 계산
        M = cv2.getPerspectiveTransform(pts_src, pts_dst)

        # 동영상 프레임을 태그 크기에 맞게 변환
        warped_frame = cv2.warpPerspective(frame, M, (img.shape[1], img.shape[0]))

        # 태그 영역에 삽입된 프레임 덮어쓰기
        mask = np.zeros_like(img, dtype=np.uint8)
        cv2.fillConvexPoly(mask, pts_dst.astype(int), (255, 255, 255))
        img = cv2.bitwise_and(img, cv2.bitwise_not(mask))
        img = cv2.bitwise_or(img, warped_frame)

    # 최종적으로 표시된 결과 출력하기
    cv2.imshow('test', img)
    key = cv2.waitKey(33)  # 약 30 FPS
    if key == 27:  # ESC 키를 누르면 종료
        break

# 자원 해제
cap.release()
vi.release()
cv2.destroyAllWindows()