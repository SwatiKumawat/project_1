#!/usr/bin/python2

import pytesseract
import pyttsx
import cv2 as cv
#import os
#from espeak import espeak
#import sys

# reading image
img = cv.imread("test.png",0)

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
