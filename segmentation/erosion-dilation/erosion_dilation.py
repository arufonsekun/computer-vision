import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys

class Segmentation(object):
    def __init__(self, img_name):
        self.RGB = cv.imread(img_name)
        self.grayScaled = cv.cvtColor(self.RGB, cv.COLOR_BGR2GRAY)
        self.smoothed = cv.GaussianBlur(self.grayScaled, (9,9), 0)
        self.core5x5 = np.ones((5,5), np.uint8)

    def plotRGB(self):
        self.__plot("RGB image", self.RGB)

    def plotGrayScale(self):
        self.__plot("Gray scale image", self.grayScaled)

    def plotSmooth(self):
        self.__plot("Smoothed image", self.smoothed)

    def plotBinarized(self):
        self.__plot("Binarized image", self.binarized)

    def plotEroded(self):
        self.__plot("Erroded image", self.eroded)

    def plotDilated(self):
        self.__plot("Dilated image", self.dilated)

    def __plot(self, message, img):
        cv.imshow(message + " press 0 to exit", img)
        cv.waitKey(0)

    def binarize(self):
        self.binarized = cv.adaptiveThreshold(self.smoothed, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 21, 5)

    def erode(self):
        self.eroded = cv.erode(self.binarized, self.core5x5, iterations=1)

    def dilate(self):
        self.dilated = cv.dilate(self.binarized, self.core5x5, iterations=1)

if __name__ == '__main__':
    imgName = sys.argv[1]
    segmentation = Segmentation(imgName)
    segmentation.binarize()
    segmentation.dilate()
    segmentation.plotDilated()
    segmentation.plotBinarized()

