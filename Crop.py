import cv2 as cv 
import numpy as np 

Image = cv.imread('Djd.jpeg')


x, y = Image.shape[:2]

top_left_I = Image[0:int(y/2) , 0:int(x/2)]

top_right_I = Image[0:int(y/2) , int(x/2):x]

bottom_left_I = Image[int(y/2):y , 0:int(x/2)]

bottom_right_I = Image[int(y/2):y , int(x/2):x]

cv.imshow('TOP_RIGHT', top_right_I)
cv.imshow('TOP_LEFT',top_left_I)
cv.imshow('BOTTOM_LEFT', bottom_left_I)
cv.imshow('BOTTOM_RIGHT', bottom_right_I)
cv.imshow('ORIGNIAL', Image)
cv.waitKey(0)
cv.destroyAllWindows()