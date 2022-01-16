# Reading and Displaying Images in OPEN CV

import cv2

# Reading Image
# Shapes of Images
# for color images flags=1, default value, or cv2.IMREAD_COLOR
#for gray flags=0 or cv2.IMREAD_GRAYSCALE
#for COLOR IMAGE not in  alpha channel flags==1 or CV2.IMREAD_UNCHANGED
# image = cv2.imread(filename=r'E:\OpenCV\OpenCV\images\DSC_2962.JPG')
#image = cv2.imread(filename=r'D:\iNeuron\OpenCV\images\DSC_2962.JPG',flags=cv2.IMREAD_COLOR)
#image = cv2.imread(filename=r'D:\iNeuron\OpenCV\images\DSC_2962.JPG',flags=cv2.IMREAD_GRAYSCALE)
image = cv2.imread(filename=r'D:\iNeuron\OpenCV\images\DSC_2962.JPG',flags=cv2.IMREAD_UNCHANGED)
print(image.shape)
cv2.imshow('deepak marriage', image)
cv2.waitKey(10000)
cv2.destroyAllWindows()


