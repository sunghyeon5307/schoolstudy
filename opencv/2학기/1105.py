# 관련 라이브러리 선언
import numpy as np
import cv2

# 영상 합성
# 영상 읽기 및 합성
img1_src = cv2.imread("./../images/img26.jpg", cv2.IMREAD_UNCHANGED)
img1 = cv2.resize(img1_src, (320, 240))
img2_src = cv2.imread("./../images/img27.jpg", cv2.IMREAD_UNCHANGED)
img2 = cv2.resize(img1_src, (320, 240))

res1 = cv2.addWeighted(img1, 0.5, img2, 0.5, 1.0)
cv2.imshow("res", res1)
cv2.imread("res_addImgs.jpg", cv2.resize(res1, (230, 240)))

#영상 스티칭
#영상 읽기
img3 = cv2.imread("./../images/img22.jpg", cv2.IMREAD_UNCHANGED)
#img3 = cv2.resize(img1_src, (320, 240))
h, w, c = img3.shape

#stitch 입력 생성
stepW = int(w/3)
overlap = int(stepW * 0.3)
sp1 = img3[:, :stepW + overlap, :]
sp2 = img3[:, stepW - overlap:(stepW * 2) + overlap, :]
sp3 = img3[:, (stepW * 2) - overlap, :]
sp1 = cv2.resize(sp1, (320, 240))
sp2 = cv2.resize(sp2, (320, 240))
sp3 = cv2.resize(sp3, (320, 240))

imgs1 = []; imgs1.append(sp1); imgs1.append(sp2)
imgs2 = []; imgs2.append(sp2); imgs1.append(sp3)
imgs3 = []; imgs3.append(sp1); imgs1.append(sp2); imgs3.append(sp3)

# stitch 생성 및 실행
stitcher = cv2.Stitcher.create(cv2.STITCHER_PANORAMA)

status1, pano1 = stitcher.stitch(imgs1)
if status1 != cv2.Stitcher_OK:
    print("Can't stitch imgs1, error code = %d" % status1)
    exit(-1)

status2, pano2 = stitcher.stitch(imgs2)
if status2 != cv2.Stitcher_OK:
    print("Can't stitch imgs2, error code = %d" % status2)
    exit(-1)

status3, pano3 = stitcher.stitch(imgs3)
if status3 != cv2.Stitcher_OK:
    print("Can't stitch imgs3, error code = %d" % status3)
    exit(-1)

#결과 영상 출력 및 저장
displays = [("input", img3),
            ("input1", sp1),
            ("input2", sp2),
            ("input3", sp3),
            ("res1", pano1),
            ("res2", pano2),
            ("res3", pano3)]
for (name, out) in displays:
    cv2.imshow(name, cv2.resize(out, (320, 240)))
    cv2.imwrite(name + ".jpg", cv2.resize(out, (320, 240)))

#키보드 입력을 기다린 후 모든 영상창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.Stitcher.stitch(imgs1)