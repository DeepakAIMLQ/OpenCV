import cv2
image1 = cv2.imread(r'E:\OpenCV\OpenCV\images\DSC_2962.JPG')
image2 = cv2.imread(r'E:\OpenCV\OpenCV\images\divi.png')

# add images
final_image=cv2.add(image1, image2)

cv2.imshow('deepak marriage', final_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()
