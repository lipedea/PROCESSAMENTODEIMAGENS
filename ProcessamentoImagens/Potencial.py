import numpy as np
import cv2

img_f = cv2.imread('imagens\seedsDark.tif', 0)

height_pixels, width_pixels = img_f.shape
neg_img_g = np.array(img_f)
c = 1
g = 1.2
for x in range(height_pixels):
    for y in range(width_pixels):
        neg_img_g[x, y] = c * np.power(img_f[x, y] , g)

cv2.imshow('image', img_f)
cv2.imshow('negative', neg_img_g)

cv2.waitKey()