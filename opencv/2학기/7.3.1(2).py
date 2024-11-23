import cv2
import numpy as np

cap = cv2.VideoCapture("/Users/bagseonghyeon/Desktop/schoolstudy/opencv/2학기/images/video2.mp4")


bgMethod1 = cv2.createBackgroundSubtractorMOG2()
bgMethod2 = cv2.createBackgroundSubtractorKNN()
bgMethod1_blur = cv2.createBackgroundSubtractorMOG2()
bgMethod2_blur = cv2.createBackgroundSubtractorKNN()

fps = cap.get(cv2.CAP_PROP_FPS)
vod1 = cv2.VideoWriter("ourput1.avi", cv2.VideoWriter_fourcc(*"MJPG"), fps, (320, 240))
vod2 = cv2.VideoWriter("ourput2.avi", cv2.VideoWriter_fourcc(*"MJPG"), fps, (320, 240))
vod3 = cv2.VideoWriter("ourput3.avi", cv2.VideoWriter_fourcc(*"MJPG"), fps, (320, 240))
vod4 = cv2.VideoWriter("ourput4.avi", cv2.VideoWriter_fourcc(*"MJPG"), fps, (320, 240))

imgIndex = 1
while(cap.isOpened()):
    ret, frame = cap.read()
    if frame is None:
        break
    
    frame = cv2.resize(frame, (320, 240))
    if imgIndex != 1:
        bgMOG = bgMethod1.getBackgroundImage()
        bgKNN = bgMethod2.getBackgroundImage()
        bgMOG_blur = bgMethod1_blur.getBackgroundImage()
        bgKNN_blur = bgMethod2_blur.getBackgroundImage()
    fgMOG = bgMethod1.apply(frame, learningRate=-1)
    fgKNN = bgMethod2.apply(frame)
    fgMOG_blur = bgMethod1_blur.apply(cv2.blur(frame, (5,5)), learningRate=-1)
    fgKNN_blur = bgMethod2_blur.apply(cv2.blur(frame, (5,5)))
    
    print(imgIndex)
    
    fgMOG_BGR = cv2.cvtColor(fgMOG, cv2.COLOR_GRAY2BGR)
    fgMOG_KNN = cv2.cvtColor(fgKNN, cv2.COLOR_GRAY2BGR)
    fgMOG_blur_BGR = cv2.cvtColor(fgMOG_blur, cv2.COLOR_GRAY2BGR)
    fgKNN_blur_BGR = cv2.cvtColor(fgKNN_blur, cv2.COLOR_GRAY2BGR)
    
    vod1.write(fgMOG_BGR)
    vod2.write(fgMOG_KNN)
    vod3.write(fgMOG_blur_BGR)
    vod4.write(fgKNN_blur_BGR)
    
    # cv2.imwrite("output/" + "mog2_" + str(imgIndex) + ".jpg", fgMOG)
    # cv2.imwrite("output/" + "knn_" + str(imgIndex) + ".jpg", fgKNN)
    # cv2.imwrite("output/" + "mog2_blur_" + str(imgIndex) + ".jpg", fgMOG_blur)
    # cv2.imwrite("output/" + "knn_blur_" + str(imgIndex) + ".jpg", fgKNN_blur)

    imgIndex += 1
    cv2.waitKey(30)
    
    if imgIndex > 100:
        break
    
    cap.release()
    vod1.release()
    vod2.release()
    vod3.release()
    vod4.release()