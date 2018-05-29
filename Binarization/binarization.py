import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys

def binarization(img, smooth):
    #Fuck pep 8
    segment = cv.adaptiveThreshold(smooth, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 21, 5)
    return (segment)

def erosion(img, core):
    erosion = cv.erode(img, core, iterations = 1)
    return (erosion)

def dilation(img, core):
    dilation = cv.dilate(img, core, iterations = 1)
    return (dilation)

def shows(array):
    out = np.vstack([
        np.hstack(array[0]),
        np.hstack(array[1])
    ])
    #English because english it's cool
    cv.imshow("Adaptative binarization", out)
    cv.waitKey(0)
#Open image, convert to gray shades, apply the smooth atribute
img  = cv.imread(sys.argv[1])
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
smooth = cv.GaussianBlur(img, (9,9), 0)#Smoothing the img

img_seg = binarization(img, smooth)

#Create core matrix
core = np.ones((5,5), np.uint8)
img_ero = erosion(img_seg, core)
img_dila = dilation(img_seg, core)
opening = dilation(img_ero, core)
closing = erosion(img_dila, core)
shows([[smooth, img_seg], [img_ero, img_dila]])
shows([[img_ero, img_dila],[closing, opening]])
