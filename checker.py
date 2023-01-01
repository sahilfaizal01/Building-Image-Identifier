import cv2

img1 = cv2.imread('train/bigben.jpeg',0)
img2 = cv2.imread('test/toronto.jpeg',0)

orb = cv2.ORB_create(nfeatures=1500)

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
imgKp1 = cv2.drawKeypoints(img1,kp1,None)
imgKp2 = cv2.drawKeypoints(img2,kp2,None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])
print(len(good))
