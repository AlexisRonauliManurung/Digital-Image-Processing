import cv2 as cv 

image = cv.imread('foto alexis.jpg', cv.IMREAD_REDUCED_COLOR_4) 
image_grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  
ret, BW = cv.threshold(image_grayscale, 120, 255, cv.THRESH_BINARY)

cv.imshow('NORMAL', image) 
cv.imshow('BINER', BW) 
cv.waitKey(0) 
cv.destroyAllWindows() 
