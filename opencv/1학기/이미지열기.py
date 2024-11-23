import cv2 as cv
img=cv.imread('img.png') # 이미지 불러오기
cv.imshow('image', img) # 이미지 보여주기('창이름' 불러온 변수이름)
cv.waitKey(0) # 키보드 입력 대기, 0은 무한대기
cv.destroyAllWindows() # 창 닫기