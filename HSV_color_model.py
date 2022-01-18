# HSV Color Model
# H=hue (red=0 or 360 degree, gree=120 degree, blue=240 degree ranges from 0 to 360
# S=saturation how much light or whiteness we need in color range from 0 (light) to 1 (dark)
# V=value how much darkness we need in color ranges 0 (dark) to 1 (light)


import cv2
image = cv2.imread(filename=r'E:\OpenCV\OpenCV\images\DSC_2962.JPG')
image=cv2.resize(image, dsize=(500,500))

cv2.imshow("deepak marriage",image)
cv2.waitKey(0)
cv2.destroyAllWindows()