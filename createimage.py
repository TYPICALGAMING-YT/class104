import numpy as np
import cv2
black=np.zeros([600,600])
print (black)
cv2.imshow("black",black)
black[200:400,200:400]=255
cv2.imshow("black and white",black)
cv2.waitKey(0)