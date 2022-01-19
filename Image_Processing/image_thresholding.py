# Image Thresholding: 1. simple threshold 2. adaptive threshold
# OpenCV Threshold OpenCV is a technique which helps in processing images.
# The threshold in OpenCV helps in assigning pixel values. These pixel values
# are allocated to threshold values.
# cv2.THRESH_BINAYR
# cv2.THRESH_BINARY_INV
# cv2.THRESH_TRUNC
# cv2.THRESH_TOZERO
# cv2.THRESH_TOZERO_INV

import cv2
image = cv2.imread(r'E:\OpenCV\OpenCV\images\DSC_2962.JPG',-1)
image=cv2.resize(image,dsize=(300,300))

# Thresh Binary => pixel  >= threshold =255 : 0
# Thresh Binary Inv => pixel >=  threshold = 0 : 255
# Thresh Trunc  => pixel >= threshold = threshhold  : remain same
# Thresh To Zero => pixel <= threshold = 0 : remain same
# Thresh To Zero Inv => pixel >= threshold = 0 : remain same

ret, thresh=cv2.threshold(src=image, thresh=100, maxval=255, type=cv2.THRESH_BINARY)
ret, thresh=cv2.threshold(src=image, thresh=100, maxval=255, type=cv2.THRESH_BINARY_INV)
ret, thresh=cv2.threshold(src=image, thresh=100, maxval=255, type=cv2.THRESH_TRUNC)
ret, thresh=cv2.threshold(src=image, thresh=100, maxval=255, type=cv2.THRESH_TOZERO)
ret, thresh=cv2.threshold(src=image, thresh=100, maxval=255, type=cv2.THRESH_TOZERO_INV)
cv2.imshow('deepak marriage', thresh)
cv2.waitKey(10000)
cv2.destroyAllWindows()
