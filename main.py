import cv2
import numpy as np
import os

orb = cv2.ORB_create(nfeatures=1500)
## iMPORT IMAGES
path = 'train'
images = []
classNames = []
myList = os.listdir(path)
print('Total Classes Detected: ',len(myList))

for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}',0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findDes(images):
    desList = []
    for img in images:
        kp, des = orb.detectAndCompute(img,None)
        desList.append(des)
    return desList

thresh = 20

def findID(img,desList):
    kp2, des2 = orb.detectAndCompute(img,None)
    bf = cv2.BFMatcher()
    matchList = []
    finalVal = -1
    try:
        for des in desList:
            matches = bf.knnMatch(des,des2,k=2)
            good = []
            for m,n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])
            matchList.append(len(good))
    except: pass
    #print(matchList)
    if len(matchList)!=0:
        if max(matchList) > thresh:
            finalVal = matchList.index(max(matchList))
    return finalVal

desList = findDes(images)
print(len(desList))

cap = cv2.VideoCapture('video.mp4')
while True:
    success, img2 = cap.read()
    imgOriginal = img2.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    id = findID(img2,desList)

    if id != -1:
        cv2.putText(imgOriginal,classNames[id],(250,250),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),3)

    cv2.imshow('img2',imgOriginal)
    cv2.waitKey(1)

cv2.destroyAllWindows()

