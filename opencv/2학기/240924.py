import os
import cv2
import numpy as np

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

# Load the image
image = cv2.imread("/Users/bagseonghyeon/Desktop/schoolstudy/opencv/2학기/images/namecard.jpeg")
orig = image.copy()

cv2.imshow("original", orig)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 1. Edge detection
ratio = 800.0 / image.shape[0]
dim = (int(image.shape[1] * ratio), 800)
image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3,3), 0)
edge = cv2.Canny(gray, 75, 200)

cv2.imshow("edge", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Find contours
(cnts, _) = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    print(len(approx))
    
    if len(approx) == 4:
        screenCnt = approx
        break

# 3. Apply perspective transform
rect = order_points(screenCnt.reshape(4, 2) * ratio)
(topLeft, topRight, bottomRight, bottomLeft) = rect

w1 = abs(bottomRight[0] - bottomLeft[0])
w2 = abs(topRight[0] - topLeft[0])

h1 = abs(topRight[1] - bottomRight[1])
h2 = abs(topLeft[1] - bottomLeft[1])

maxWidth = max([w1, w2])
maxHeight = max([h1, h2])

dst = np.tloat32([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight -1], [0, maxHeight - 1]])
M = cv2.getPerspectiveTransform(rect, dst)
cv2.waitKey(0)
