import cv2
#
# Reading the image
img = cv2.imread('Pictures/Test/Test2.jpg')

# Converting image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Loading the required haar-cascade xml classifier file
haar_cascade = cv2.CascadeClassifier('Pictures/classifier/cascade.xml')

# Applying the face detection method on the grayscale image
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

# Iterating through rectangles of detected faces
for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Detected faces', img)

cv2.waitKey(0)


#here is code to check the output
import cv2
face_cascade=cv2.CascadeClassifier(r"F:\data imp\coding\Opencv\data_Downlode\data of cats\classifier\cascade.xml")###path of cascade file
## following is an test image u can take any image from the p folder in the temp folder and paste address of it on below line
img= cv2.imread(r"F:\data imp\coding\Opencv\data_Downlode\data of cats\p\1588088937587.jpg")###path of image file which we want to detect
resized = cv2.resize(img,(400,200))
gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,6.5,17)#try to tune this 6.5 and 17 parameter to get good result
##if not getting good result try to train new cascade.xml file again deleting other file expect p and n in temp folder
for(x,y,w,h) in faces:
    resized=cv2.rectangle(resized,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('img',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()