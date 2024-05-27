import cv2
img=cv2.imread("butterfly.jpg")
print (img)
cv2.imshow("butterfly",img)

grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayimage",grayimg)
print(grayimg)
cv2.waitKey(0)