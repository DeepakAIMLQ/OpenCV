import cv2
image = cv2.imread(filename=r'E:\OpenCV\OpenCV\images\DSC_2962.JPG')
image=cv2.resize(image, dsize=(500,500))

image=cv2.ellipse(img=image, center=(200,200), axes=(50,70),
                  angle=90,thickness=5, startAngle=0, endAngle=360, color=(255,52,41) )
cv2.imshow("deepak marriage",image)
cv2.waitKey(0)
cv2.destroyAllWindows()