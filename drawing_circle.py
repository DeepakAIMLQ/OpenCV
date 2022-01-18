import cv2
image = cv2.imread(filename=r'E:\OpenCV\OpenCV\images\DSC_2962.JPG')
image=cv2.resize(image, dsize=(500,500))
center=(200,200)
radius=40
color=(255,52,0)
thikness= 5   #vaue in minus like -1,-2 etc will be solid color circle

image=cv2.circle(img=image,center=center, radius=radius,color=color, thickness=thikness, lineType=cv2.LINE_4)
cv2.imshow("deepak marriage",image)
cv2.waitKey(0)
cv2.destroyAllWindows()