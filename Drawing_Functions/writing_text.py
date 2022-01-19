import cv2
image = cv2.imread(filename=r'E:\OpenCV\OpenCV\images\DSC_2962.JPG')
image=cv2.resize(image, dsize=(500,500))

text1="Welcome to AIMLQ.DEEPAK"
text2="in GITHUB account"
cv2.putText(img=image, text=text1, org=(0,25), fontFace=cv2.FONT_ITALIC,
            fontScale=1, color=(0,0,255), thickness=4, lineType=cv2.LINE_AA)


cv2.putText(img=image, text=text2, org=(20,50), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1, color=(0,0,255), thickness=4, lineType=cv2.LINE_AA)

cv2.imshow("deepak marriage",image)
cv2.waitKey(0)
cv2.destroyAllWindows()