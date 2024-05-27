import cv2
poster=cv2.imread("poster.jpg")
print(poster)
cv2.imshow("poster.jpg",poster)
rocket=poster[120:360,400:500]
cv2.imshow("rocketimage",rocket)
poster[0:240,500:600]=rocket

text_to_show="Hi!,im aditya"
txt_to_show="im in Grade XII"
cv2.putText(poster,text_to_show,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))
cv2.putText(poster,txt_to_show,(30,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(100,10,145))
cv2.imshow("editedimages",poster)
cv2.waitKey(0)
