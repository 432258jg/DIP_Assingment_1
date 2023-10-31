import cv2
#code for pictures
'''

# Reading the image
img = cv2.imread('Pictures/Test/Clutter.jpg')
# Converting image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Loading the required haar-cascade xml classifier file
#haar_cascade = cv2.CascadeClassifier('Pictures/classifier/cascade.xml')
#haar_cascade = cv2.CascadeClassifier('Pictures/cascade_zoomedIn.xml')
haar_cascade = cv2.CascadeClassifier('Pictures/haarcascade_frontalface_default.xml')
# Applying the face detection method on the grayscale image
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

# Iterating through rectangles of detected faces
for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Detected faces', img)
cv2.waitKey(0)
'''
# To capture video from webcam
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('Pictures/cascade_zoomedIn.xml')
#Creating a loop to capture each frame of the video in the name of Img
while True:
    _,img = cap.read()

    #Converting to grey scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Allowing multiple face detection
    faces = face_cascade.detectMultiScale(gray_img, 1.1, 6)

    #Creating Rectangle around face
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 250), 2)

    #Displaying the image
    cv2.imshow('Detected Face Image',  img)

    #Waiting for escape key for image to close adding the break statement to end the face detection screen
    k = cv2.waitKey(30) & 0xff
    if k == 81 or k == 113:
        break

#'''