import cv2

#color RGB/BGR
# opencv take colours in bgr format
#white 255,255,255
#black 0,0,0
# red 255,0,0
# green 0,255,0
# blue 0,0,255

# Accessing Pixel Values
image = cv2.imread(filename=r'D:\iNeuron\OpenCV\images\DSC_2962.JPG')
image=cv2.resize(image, dsize=(500,500))
# acecss image pixels for size is 500,500
image[0:50,0:50]=[45,255,60]
print(image)
cv2.imshow("deepak marriage",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
