import numpy as np
import cv2
import sys

class DiceRollingCounter():
    def __init__(self, img):
        self.RGB = cv2.imread(img)
        self.__resize(400)
        self.grayScale = cv2.cvtColor(self.RGB, cv2.COLOR_BGR2GRAY)
        self.grayScaleCopy = self.grayScale.copy()
        self.fontFamily = cv2.FONT_HERSHEY_SIMPLEX

    def __resize(self, baseWidth):
        height, width, channels = self.RGB.shape
        scale = width / height
        self.RGB = cv2.resize(self.RGB, (baseWidth, int(baseWidth / scale)))

    def smooth(self):
        self.smoothed = cv2.GaussianBlur(self.grayScale, (7,7), 0)

    def detectEdges(self):
        self.edges = cv2.Canny(self.smoothed, 200, 350)
    
    def __write(self, img, text, color = (255, 0, 0)):
        cv2.putText(img, text, (10, 20), self.fontFamily, 0.5, color, 0, cv2.LINE_AA)

    def countContourns(self):
        (self.objects, self.lx) = cv2.findContours(self.edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.__write(self.grayScale, "Gray scale image", 0)
        self.__write(self.smoothed, "Smoothed image with Gaussian operator", 0)
        self.__write(self.edges, "Edge detected image using Canny algorithm", 255)
        self.__drawContourns()

    def __drawContourns(self):
        cv2.drawContours(self.grayScaleCopy, self.objects, -1, (255,255,255), 2)
        self.__write(self.grayScaleCopy, "Rolling result: " + str(len(self.objects)), 0)

    def plot(self):
        self.imagesJoined = np.vstack([
            np.hstack([self.grayScale, self.smoothed]),
            np.hstack([self.edges, self.grayScaleCopy])
        ])
        cv2.imshow("Result", self.imagesJoined)
        cv2.waitKey()

if __name__ == '__main__':
    counter = DiceRollingCounter(sys.argv[1])
    counter.smooth()
    counter.detectEdges()
    counter.countContourns()
    counter.plot()