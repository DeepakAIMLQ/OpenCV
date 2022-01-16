import cv2
#Draw line cv2.line()
image = cv2.imread(filename=r'D:\iNeuron\OpenCV\images\DSC_2962.JPG')
image=cv2.resize(image, dsize=(500,500))
cv2.line(img=image, pt1=(0,0),pt2=(100,100),color=(0,255,0), thickness=5)
cv2.line(img=image, pt1=(100,100),pt2=(0,450),color=(0,255,255), thickness=10)

# arrow
cv2.arrowedLine(img=image, pt1=(0,450),pt2=(100,0),color=(0,255,100), tipLength=0.2, thickness=10)
cv2.imshow("deepak marriage",image)
cv2.waitKey(0)
cv2.destroyAllWindows()