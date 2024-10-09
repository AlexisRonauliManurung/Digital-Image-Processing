import cv2 as cv 


image = cv.imread('foto alexis.jpg', cv.IMREAD_REDUCED_COLOR_4) 
image_grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY) 

cv.imshow('NORMAL', image) 
cv.imshow('GRAYSCALE', image_grayscale) 

cv.waitKey(0) 
cv.destroyAllWindows() 

