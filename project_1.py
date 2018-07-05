#!/usr/bin/python2
import pytesseract
import os
import cv2 as cv
from espeak import espeak
import sys
img = cv.imread("a.png",0)

config = ('-l eng --oem 1 --psm 3')

text = pytesseract.image_to_string(img, config=config)
print text

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

