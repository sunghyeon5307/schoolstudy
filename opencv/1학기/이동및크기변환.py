import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("/Users/bagseonghyeon/Desktop/schoolstudy/opencv/images/img11.jpg", cv2.IMREAD_GRAYSCALE)

h, w, = img1.shape
tlans_x = 10; tlans_y = 25
point1_src = np.float32([[15,20], [50,70], [130,140]])
point1_dst = np.float32(point1_src + [tlans_x, tlans_y])
affine_mat1 = cv2.getAffineTransform(point1_src, point1_dst)
user_mat1 = np.float32([[1,0,tlans_x], [0,1,tlans_y]])
res1 = cv2.warpAffine(img1, affine_mat1, (w,h))
res2 = cv2.warpAffine(img1, user_mat1, (w,h))

scale_x = 0.8; scale_y = 0.6
user_mat2 = np.float32([[scale_x, 0, 0], [0, scale_y, 0]])
res3 = cv2.warpAffine(img1, user_mat2, (w, h))
res4 = cv2.resize(img1, (0,0), None, scale_x, scale_y)
background = np.full(shape=[h,w], fill_value=0, dtype=np.uint8)
background[:round(h*scale_y), :round(w*scale_x)] = res4;
res4 = background

user_mat3 = np.float32([[0.4, 0, 100], [0, 0.6, 50]])
res5 = cv2.warpAffine(img1, user_mat3, (w,h))

ress = []
ress.append(img1), ress.append(res1), ress.append(res2)
ress.append(res3), ress.append(res4), ress.append(res5)
titles = ['input', 'res1', 'res2', 'res3', 'res4', 'res5']

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(ress[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()