import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys

#Lê o arquivo converte valores para inteiro e estrutura a matriz
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
    #Valores que acessam o elemento "esquerda superior" a partir do elemento de referência
    img_i = stride[0] - factor
    img_j = stride[1] - factor
    sum = 0
    count = 0
    kernel_i = 0
    kernel_j = 0
    while count < len(kernel)**2:
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

def convolution(img, file, step):
    gray_img = cv.cvtColor(cv.imread(img), cv.COLOR_BGR2GRAY)
    #Cria a matriz kernel a partir do arquivo
    kernel = create_kernel(file)

    #Distância entre o pixel de referência (pixel do stride) e os pixels mais externos
    factor = len(kernel) // 2

    #Lista com o pixel de referencia
    stride = [factor, factor]

    convolution_matrix = []
    convolution_row = []

    count_line = 1
    count_column = 1

    while count_line <= ((len(gray_img) - (factor * 2)) // step) - 1:
        if count_column == ((len(gray_img[0]) - (factor * 2)) // step) + 1:
            count_column = 1
            stride[0] += step
            stride[1] = factor
            convolution_matrix.append(convolution_row)
            convolution_row = []
            count_line += 1

        count_column += 1
        summ =  multiplies(stride, gray_img, factor, kernel)
        convolution_row.append(summ)
        stride[1] += step


    #Converte a matriz do python para uma matriz do numpy
    img_out8 = np.uint8(convolution_matrix)
    img_out16 = np.uint16(convolution_matrix)
    img_out32 = np.uint32(convolution_matrix)

    #Plota as imagens
    plt.subplot(2,2,1),plt.imshow(gray_img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(img_out8,cmap = 'gray')
    plt.title('uint8'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(img_out16,cmap = 'gray')
    plt.title('uint16'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(img_out32,cmap = 'gray')
    plt.title('uint32'), plt.xticks([]), plt.yticks([])
    plt.show()
    cv.waitKey(0)
#Ordem dos parametros: imagem(.png,.jpeg,) arquivo do kernel(.txt) e stride(int)
convolution(sys.argv[1], sys.argv[2], int(sys.argv[3]))
