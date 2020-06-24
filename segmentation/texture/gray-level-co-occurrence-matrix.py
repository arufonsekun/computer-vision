import cv2 as cv
import numpy as np
import scipy
from skimage.feature import greycomatrix, greycoprops
import sys

class GLCMFeatures():
    def __init__(self, fileName):
        if fileName == None:
            print("No such file")
            return

        self.fileName = fileName
        self.videoReader = cv.VideoCapture(fileName)
        self.windowName = "Gray Level Co-occurrence Matrix Features"
        self.reading = True
        self.original = None
        self.glcm = None
        self.gray = None
        self.dimention = ()
        self.frameScale = 3
        self.directions = [0, np.pi/4, np.pi/2, 3*np.pi/4]
        self.features = {"contrast", "dissimilarity", "homogeneity", 
        "ASM", "energy", "correlation"}
        self.distances = [1]

        if self._fileExits():
            self.__main__()

    def _fileExits(self):
        return self.videoReader.isOpened()

    def _resize(self):
        self.dimention = (int(self.original.shape[1] / self.frameScale), int(self.original.shape[0] / self.frameScale))
        self.original = cv.resize(self.original, self.dimention, interpolation = cv.INTER_AREA)

    def _cvtGray(self):
        self.gray = cv.cvtColor(self.original, cv.COLOR_BGR2GRAY)

    def _computeGLCM(self):
        self.glcm = greycomatrix(self.gray, self.distances, self.directions, levels=256, normed=True, symmetric=True)

    def _getContrast(self):
        self.contrast = greycoprops(self.glcm, 'contrast')

    def __main__(self):
        while self.videoReader.isOpened():
            hasFrame, self.original = self.videoReader.read()

            if not hasFrame:
                break

            self._resize()
            self._cvtGray()
            self._computeGLCM()
            self._getContrast()

            print(self.contrast)

            cv.imshow(self.windowName, self.gray)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        self.videoReader.release()
        cv.destroyAllWindows()

if __name__ == '__main__':
    try:
        fileName = sys.argv[1]
        glcm = GLCMFeatures(fileName)
    except IndexError:
        print("No such file")
