import numpy as np
import cv2

img_f = cv2.imread('imagens\seedsDark.tif', 0)

height_pixels, width_pixels = img_f.shape
neg_img_g = np.array(img_f)

print("Quanto de brilho deseja aumentar?")
k = input()
k = int(k)
for x in range(height_pixels):
    for y in range(width_pixels):
            if k + img_f[x,y] <= 255:
                neg_img_g[x, y] = (img_f[x, y] + k)
            else:
                neg_img_g[x,y] = 255
cv2.imshow('image', img_f)
cv2.imshow('negative', neg_img_g)

cv2.waitKey()