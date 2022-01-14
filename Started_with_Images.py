# Reading and Displaying Images in OPEN CV

import cv2

# Reading Image

image = cv2.imread(filename=r'E:\OpenCV\OpenCV\images\DSC_2962.JPG')
cv2.imshow('deepak marriage', image)
cv2.waitKey(10000)
cv2.destroyAllWindows()