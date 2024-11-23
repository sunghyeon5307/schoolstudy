import cv2
import numpy as np

img = np.full(shape=(600,800,3), fill_value=255, dtype=np.uint8)

font_italic = "FONT_ITALIC"
font_hershey_plain = "FONT_HERSHEY_PLAIN"
font_hershey_complex = "FONT_HERSHEY_COMPLEX"
font_hershey_complex_small = "FONT_HERSHEY_COMPLEX_SMALL"
font_hershey_duplex = "FONT_HERSHEY_DUPLEX"
font_hershey_script_complex = "FONT_HERSHEY_SCRIPT_COMPLEX"
font_hershey_script_simplex = "FONT_HERSHEY_SCRIPT_SIMPLEX"
font_hershey_simplex = "FONT_HERSHEY_SIMPLEX"
font_hershey_triplex = "FONT_HERSHEY_TRIPLEX"

cv2.putText(img, font_italic, (50,50), cv2.FONT_ITALIC, 1, (255,0,0),2)
cv2.putText(img, font_hershey_plain, (50,100), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0),2)
cv2.putText(img, font_hershey_complex, (50,150), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
cv2.putText(img, font_hershey_complex_small, (50,200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255),2)
cv2.putText(img, font_hershey_duplex, (50,250), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,0),2)
cv2.putText(img, font_hershey_script_complex, (50,300), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255,0,255),2)
cv2.putText(img, font_hershey_script_simplex, (50,350), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,255,255),2)
cv2.putText(img, font_hershey_simplex, (50,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (51,102,0),2)
cv2.putText(img, font_hershey_triplex, (50,450), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,153,255),2)
