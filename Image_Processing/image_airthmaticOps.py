import cv2
image1 = cv2.imread(r'D:\iNeuron\OpenCV\images\DSC_2962.JPG')
image1=cv2.resize(image1,dsize=(400,400))
image2 = cv2.imread(r'D:\iNeuron\OpenCV\images\divi.png')
image2=cv2.resize(image2,dsize=(400,400))

final_image=cv2.addWeighted(src1=image1, alpha=1, src2=image2, beta=0.5,gamma=10) #add gama for whiteness
# add images
# final_image=cv2.add(image1, image2)
# divide images
# final_image=cv2.divide(image1, image2, scale=25)   #scale value multiple result so that pic not become black(0)
# cv2.addWeighted()
# cv2.divide()
# cv2.subtract()
# cv2.multiply()

cv2.imshow('deepak marriage', final_image)
cv2.waitKey(10000)
cv2.destroyAllWindows()
