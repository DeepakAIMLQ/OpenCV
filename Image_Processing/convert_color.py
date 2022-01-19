# cv2.cvtColor(image,code=cv2.COLOR_RGB etc.


import cv2
image = cv2.imread(r'E:\OpenCV\OpenCV\images\DSC_2962.JPG',-1)
image=cv2.resize(image,dsize=(300,300))

image=cv2.cvtColor(image,cv2.COLOR_HSV2RGB)

cv2.imshow('deepak marriage', image)
cv2.waitKey(10000)
cv2.destroyAllWindows()
