import cv2 as cv

image = cv.imread('foto alexis.jpg', cv.IMREAD_REDUCED_COLOR_4)

ksize = (5, 5)
sigma = 1.0
filtered_image = cv.blur(image, ksize, sigma)

cv.imshow('NORMAL', image)
cv.imshow('FILTERED', filtered_image)
cv.waitKey(0)
cv.destroyAllWindows()
