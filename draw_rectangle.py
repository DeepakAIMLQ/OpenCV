import cv2
image = cv2.imread(filename=r'E:\OpenCV\OpenCV\images\DSC_2962.JPG')
image=cv2.resize(image, dsize=(500,500))

image=cv2.rectangle(img=image,pt1=(50,50), pt2=(150,150), thickness=-1, color=(0,0,255),
                    lineType=cv2.LINE_AA)
cv2.imshow("deepak marriage",image)
cv2.waitKey(0)
cv2.destroyAllWindows()