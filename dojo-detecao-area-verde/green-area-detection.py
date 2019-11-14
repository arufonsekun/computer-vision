import cv2
import numpy as np
from functools import reduce

resize = lambda img: cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

def dstretch(A, tol=None):
    orig_shape = A.shape
    A = A.reshape((-1, 3)).astype(np.float)
    covariance = np.cov(A.T)
    sigman = np.diag(np.sqrt(covariance.diagonal()))
    eigenValue, eigenVector = np.linalg.eig(covariance)
    stretch = np.diag(1 / np.sqrt(eigenValue))
    mean = np.mean(A, axis = 0)
    A -= mean
    T = reduce(np.dot, [sigman, eigenVector, stretch, eigenVector.T])
    offset = mean - np.dot(mean, T)
    A = np.dot(A, T)
    A += mean + offset
    B = A.reshape(orig_shape)

    for channel in range(3):
        if tol:
            low, high = np.percentline(B[:,:,channel],100 - 100 * tol)
            B[B < low] = low
            B[B > high] = high
        B[:,:,channel] = 255 * (B[:,:,channel] - B[:,:,channel].min()) / (B[:,:,channel].max() - B[:,:,channel].min())

    return B.astype(np.uint8)

img = resize(cv2.imread('area-verde.png'))

blur_intensity = 5

#kernel = np.ones((blur_intensity, blur_intensity), np.float32) / (blur_intensity**2)
#gaussian = cv2.filter2D(img, -1, kernel)

gaussian = cv2.blur(img, (blur_intensity, blur_intensity))
saturated = dstretch(img)

cv2.imshow('Gaussian blur', gaussian)
cv2.imshow('Original Image', img)
cv2.imshow('saturated', saturated)
cv2.waitKey(0)
cv2.destroyAllWindows()
