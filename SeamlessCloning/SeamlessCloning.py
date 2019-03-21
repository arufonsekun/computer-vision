
import cv2
import numpy as np

# Leitura das Imagens
src = cv2.imread('input/airplane.jpg')
dst = cv2.imread('input/sky.jpg')

# Criando a mascara do obejeto
#mask = np.zeros(src.shape, src.dtype)
mask = 255 * np.ones(src.shape, src.dtype)
poly = np.array([[4,80], [30,54], [151, 63], [298, 90], [272,134], [43, 122]], np.int32)
mask = cv2.fillPoly(mask, [poly], (255, 255, 255))

# Definindo local do objeto
width, height, _ = dst.shape
place = (600,100)
#place = (int(width / 2), int(height / 2))

# Clone seamlessly.
output_normal = cv2.seamlessClone(src, dst, mask, place, cv2.NORMAL_CLONE)
output_mixed = cv2.seamlessClone(src, dst, mask, place, cv2.MIXED_CLONE)
output_monochrome_transfer = cv2.seamlessClone(src, dst, mask, place, cv2.MONOCHROME_TRANSFER)

# Mostar os resultados
resize = lambda img: cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Destino", resize(dst))
cv2.imshow("Sobreposta", resize(src))
cv2.imshow("SEAMLESS NORMAL_CLONE", resize(output_normal))
cv2.imshow("SEAMLESS MIXED_CLONE", resize(output_mixed))
cv2.imshow("SEAMLESS MONOCHROME_CLONE", resize(output_monochrome_transfer))

cv2.waitKey(0)
cv2.destroyAllWindows()
