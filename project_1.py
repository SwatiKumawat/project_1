#!/usr/bin/python2

import pytesseract
import pyttsx
import cv2 as cv
#import os
#from espeak import espeak
#import sys

# reading image
img = cv.imread("test.png")
#converting image to gray
bw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#applying thresholding on a white background image
ret,thresh = cv2.threshold(bw,150,255,cv2.THRESH_BINARY)
adapt_thresh = cv2.adaptiveThresold(bw,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

# cleaning black image 
th,dst = cv2.threshold(bw,50,255,cv2.THRESH_BINARY_INV)

#showing the images 
cv2.imshow("original",img)
cv2.imshow("grayimg",bw)
cv2.imshow("thresholded",thresh)
cv2.imshow("adaptive",adapt_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

config = ('-l eng --oem 1 --psm 3')
#converting image text to string
text = pytesseract.image_to_string(img, config=config)
#printing the extracted text
print text

#say the text from image
engine=pyttsx.init()
engine.say(text)
engine.runAndWait()

'''
a=text.decode('utf-8')
#a = text.split(' ')
espeak.synth(a)

li = text.split(' ')
#print type(li)
for i in li:
	#print li
	#print i
	#print i.decode('utf-8')
	espeak.synth(i)
'''
