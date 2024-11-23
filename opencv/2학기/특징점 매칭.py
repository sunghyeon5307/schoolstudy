
import cv2
import numpy as np

mouseDrawing = False
startX, startY, endX, endY = -1, -1, -1, -1
minMatchCount = 1
viewName = 'input image'

#특징 선언
# sift = cv2.xfeatures2d. SIFT_create()
# surf = cv2.xfeatures2d.SURF_create()
brisk = cv2.BRISK_create()
orb = cv2.ORB_create()

# Brute-Force
def BruteForce (img1, img2):
    methods = [ #(sift, cv2.NORM_L2, 'bf_sift'),
                # (surf, cv2.NORM_L2, 'bf_surf'),
                (brisk, cv2.NORM_L2, 'bf_brisk'),
                (orb, cv2.NORM_HAMMING, 'bf_orb')]
    flag = cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    
    for (method, dist, name) in methods:
        keyP1, des1 = method.detectAndCompute (img1, None) 
        keyP2, des2 = method.detectAndCompute(img2, None)
    
    #Brute Force 선언 및 매칭 수행
    bf = cv2.BFMatcher_create(dist, True)
    mat = bf.match(des1, des2)
    mat = sorted(mat, key=lambda x:x.distance)
    res = cv2.drawMatches (img1, keyP1, img2, keyP2, mat[0:20], None, flags=flag) 
    cv2.imshow(name, res)
    
    bfKnn = cv2.BFMatcher()
    matKnn = bfKnn.knnMatch(des1, des2, k = 2)
    
    #매칭 결과 선별
    good = []
    for m, n in matKnn:
        if m.distance < 0.75 * n.distance:
            good.append(m)
            
    #기하학적 관계 기반의 매칭 결과 선별
    if len(good) >= minMatchCount:
        img1KP = np.float32([keyP1 [m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        img2KP = np.float32([keyP2 [m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        _m, mask = cv2.findHomography (img1KP, img2KP, cv2.RANSAC, 5.0)
        ransacMask = mask.ravel().tolist()
        drawParams = dict(matchColor=(0, 255, 0),
                        singlePointColor=(0, 0, 255),
                        matchesMask=ransacMask [0:20],
                        flags=flag)
        
        resKnn = cv2.drawMatchesKnn(img1, keyP1, img2, keyP2, [good [0:20]], None, flags=flag) 
        resKnn2 = cv2.drawMatches (img1, keyP1, img2, keyP2, good [0:20], None, **drawParams)
        
        cv2.imshow(name+"Knn", resKnn)
        cv2.imshow(name + "KnnRansac", resKnn2)
        
    #--- FLANN 기반 매칭
    def flann (img1, img2):
        #flann 변수 설정
        flannIndexKdtree = 1
        indexParmaskdtree = dict(algorithm=flannIndexKdtree, trees=5)
        searchParms = dict(checks=50)
        flannkdtree = cv2.FlannBasedMatcher (indexParmaskdtree, searchParms)
        
        flannIndexLsh = 6
        indexParmasLsh = dict(algorithm=flannIndexLsh,
                            table_number = 6,
                            key_size = 12,
                            multi_probe_level = 1)
        flannLsh = cv2.FlannBasedMatcher (indexParmasLsh, searchParms)
        
        methods = [ #(sift, flannkdtree, 'flann_sift'),
                    # (surf, flannkdtree, 'flann_surf'),
                    (brisk, flannLsh, 'flann_brisk'), 
                    (orb, flannLsh, 'flann_orb')]
        
        for (method, matcher, name) in methods:
            keyP1, des1 = method. detectAndCompute(img1, None) 
            keyP2, des2 = method.detectAndCompute (img2, None)
            mat = matcher.match(des1, des2)
            mat = sorted (mat, key=lambda x: x.distance)
            res = cv2.drawMatches(img1, keyP1, img2, keyP2, mat [0:20], None, 
                                  flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            cv2.imshow(name, res)