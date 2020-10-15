import numpy as np
import cv2

img_f = cv2.imread('imagens\seedsHighContrast.tif', 0)

height_pixels, width_pixels = img_f.shape
neg_img_g = np.array(img_f)

print("Em qual intensidade de cinza de 0 - 255 deseja trabalhar? ")

i = 70
for x in range(height_pixels):
    for y in range(width_pixels):
        if img_f[x,y] <= i:
            neg_img_g[x, y] = 0

cv2.imshow('image', img_f)
cv2.imshow('negative', neg_img_g)

cv2.waitKey()