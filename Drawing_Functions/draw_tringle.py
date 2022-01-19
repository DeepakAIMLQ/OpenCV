import cv2
image = cv2.imread(filename=r'E:\OpenCV\OpenCV\images\DSC_2962.JPG')
image=cv2.resize(image, dsize=(500,500))

point1=(350,200)
point2=(100,450)
point3=(400,360)

cv2.line(img=image,pt1=point1,pt2=point2, color=(255,0,0), thickness=5)
cv2.line(img=image,pt1=point2,pt2=point3, color=(255,0,0), thickness=5)
cv2.line(img=image,pt1=point3,pt2=point1, color=(255,0,0), thickness=5)

center_point=((point1[0]+point2[0]+point3[0])//3, (point1[1]+point2[1]+point3[1])//3)
cv2.circle(img=image,center=center_point,radius=10,color=(0,255,0), thickness=5)



cv2.imshow("deepak marriage",image)
cv2.waitKey(0)
cv2.destroyAllWindows()