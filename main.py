import cv2
import numpy as np

"""gamma
def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)


img = cv2.imread('test.jpg')
img_output = gammaCorrection(img, 1.2)

compare = np.concatenate((img, img_output), axis=1)

cv2.imshow('Original image', img)
cv2.imshow('Gamma corrected image', img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""Histogram equalization
img = cv2.imread('test3.jpg')
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

compare = np.concatenate((img, img_output), axis=1)

cv2.imshow('Original image', img)
cv2.imshow('Output image', img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""Gaussian filter
img = cv2.imread('test3.jpg')

img_output = cv2.GaussianBlur(img, (5,5), cv2.BORDER_DEFAULT)
# img_output = cv2.GaussianBlur(img,(9,9),cv2.BORDER_REFLECT_101)

compare = np.concatenate((img, img_output), axis=1)

cv2.imshow('Original image', img)
cv2.imshow('Output image', img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""Median filter"""
img = cv2.imread('test3.jpg')

img_output = cv2.medianBlur(img, 5)
#laplacian = cv2.Laplacian(img,cv2.CV_64F)
compare = np.concatenate((img, img_output), axis=1)

#cv2.imshow('Original image', img)
cv2.imshow('Output image', compare)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""Laplacian filter
img = cv2.imread('test3.jpg')

#img_output = cv2.medianBlur(img, 5)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
compare = np.concatenate((img, laplacian), axis=1)

#cv2.imshow('Original image', img)
cv2.imshow('Output image', compare)
cv2.waitKey(0)
cv2.destroyAllWindows()"""