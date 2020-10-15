import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('imagens\FOBOS.tif',0)

height_pixels, width_pixels = np.shape(img)
img_Equalizada = cv2.equalizeHist(img)

valores = [0]*256
valoresE = [0]*256
intensidade = []


for i in range(256):
    intensidade.append(i)

for x in range(height_pixels):
    for y in range(width_pixels):
            valores[(img[x, y])] += 1

for x in range(height_pixels):
    for y in range(width_pixels):
            valoresE[(img_Equalizada[x, y])] += 1



cv2.imshow("Imagem original", img)
cv2.imshow("img equalizada",img_Equalizada)

cv2.waitKey()


plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(intensidade, valores)
plt.hist(img.ravel(),256,[0,256])


plt.show()

plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(intensidade, valoresE)
plt.hist(img_Equalizada.ravel(),256,[0,256])

plt.show()



mamo = cv2.imread('imagens\mamo.tif',0)
mamo = cv2.equalizeHist(mamo)
hp, wp = np.shape(mamo)

valoresM = [0]*256
intensidadeM = []

for i in range(256):
    intensidadeM.append(i)

for x in range(hp):
    for y in range(wp):
            valoresM[(mamo[x, y])] += 1

plt.title("Histograma Equalizado mamografia")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(intensidadeM, valoresM)
plt.hist(mamo.ravel(),256,[0,256])

plt.show()