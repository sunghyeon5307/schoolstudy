import cv2
import numpy as np
import random

# 초기 설정
canvas = np.ones((600, 800, 3), dtype=np.uint8) * 255  # 흰색 캔버스 생성
drawing = False  # 마우스 드래그 중인지 여부
start_x, start_y = -1, -1  # 원의 시작 좌표 초기화

# 원 그리기 함수
def draw_circle(event, x, y, flags, param):
    global start_x, start_y, drawing, canvas

    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스 왼쪽 버튼 누름
        drawing = True
        start_x, start_y = x, y  # 시작점 기록

    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 이동 중
        if drawing:
            # 드래그하면서 실시간으로 원을 시각화
            temp_canvas = canvas.copy()
            radius = int(((x - start_x) ** 2 + (y - start_y) ** 2) ** 0.5)  # 반지름 계산
            random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # 랜덤 색상 생성
            cv2.circle(temp_canvas, (start_x, start_y), radius, random_color, 2)  # 임시 캔버스에 원 그리기
            cv2.imshow('Canvas', temp_canvas)

    elif event == cv2.EVENT_LBUTTONUP:  # 마우스 왼쪽 버튼 뗌
        drawing = False
        # 마우스 버튼을 떼면 원을 그림
        radius = int(((x - start_x) ** 2 + (y - start_y) ** 2) ** 0.5)  # 반지름 계산
        if radius > 0:
            random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # 랜덤 색상 생성
            cv2.circle(canvas, (start_x, start_y), radius, random_color, 2)  # 실제 캔버스에 원 그리기
            cv2.imshow('Canvas', canvas)

# 윈도우 생성 및 콜백 설정
cv2.namedWindow('Canvas')
cv2.setMouseCallback('Canvas', draw_circle)

# 초기 캔버스 보여주기
cv2.imshow('Canvas', canvas)

# 키 입력 대기 루프
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC 키를 누르면 종료
        break

# 윈도우 종료
cv2.destroyAllWindows()