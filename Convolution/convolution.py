import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys

#Read the file e estructure de kernel matrix
def create_kernel(file):
    kernel_file = open(file,'r').read().splitlines()
    matrix_string = []
    matrix_int = []
    row = []
    for e in kernel_file:
        matrix_string.append(e.split(' '))
    i = 0
    j = 0
    count = 0
    while count < len(matrix_string[0]) * len(matrix_string):
        row.append(int(matrix_string[i][j]))
        count += 1
        j += 1
        if len(row) == len(matrix_string):
            j = 0
            i += 1
            matrix_int.append(row)
            row = []
    return(matrix_int)

def multiplies(stride, gray_img, factor, kernel):
    img_i = stride[0] - factor
    img_j = stride[1] - factor
    sum = 0
    count = 0
    #row and column to access the kernel
    kernel_i = 0
    kernel_j = 0
    while count <= 8:
        if kernel_j == len(kernel):
            kernel_i += 1
            kernel_j = 0
            img_i += 1
            img_j = stride[1] - factor
        count += 1
        sum += kernel[kernel_i][kernel_j] * gray_img[img_i][img_j]
        img_j += 1
        kernel_j += 1
    return sum

def convolution(img, file):
    gray_img = cv.cvtColor(cv.imread(img), cv.COLOR_BGR2GRAY)
    kernel = create_kernel(file)
    factor = len(kernel) // 2
    stride = [factor, factor]
    convolution_matrix = []
    convolution_row = []
    #nº of iterations
    #n = (len(gray_img) - ((len(kernel) // 2) * 2)) * (len(gray_img[0]) - ((len(kernel) // 2) * 2))
    while stride[0] != len(gray_img) - factor -1:
        if stride[1] == len(gray_img[0]) - factor - 1:
            stride[0] += 1
            stride[1] = factor
            convolution_matrix.append(convolution_row)
            convolution_row = []
        summ =  multiplies(stride, gray_img, factor, kernel)
        convolution_row.append(summ)
        stride[1] += 1
    #print(convolution_matrix)
    img_out = np.uint8(convolution_matrix)
    #print(gray_img[0])
    #print(gray_img[1])
    #print(gray_img[2])
    #print(convolution_matrix[0])
    #cv.imshow("Imagem original", gray_img)
    plt.subplot(2,2,1),plt.imshow(gray_img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(img_out,cmap = 'gray')
    plt.title('Convolution'), plt.xticks([]), plt.yticks([])
    plt.show()
    cv.waitKey(0)
    plt.close('all')
convolution(sys.argv[1], sys.argv[2])
#print(create_kernel(sys.argv[2]))
