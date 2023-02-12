# image detection in python
# get xml pretrained file from github below
# https://github.com/opencv/opencv/tree/master/data/haarcascades

import cv2 
import numpy as np 

# Read image 
img = cv2.imread('data/street.jpg') 
  
# Convert to grayscale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Detect faces 
faces = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml').detectMultiScale(gray, 1.2, 5) 
  
print(len(faces))
for (x, y, w, h) in faces:      # Draw rectangle around the face 
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2) 

    # Display the output  
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
