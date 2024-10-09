import cv2

image = cv2.imread('nadifah.jpg', 0)  # Load the image as grayscale

equalized_image = cv2.equalizeHist(image)

cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original Image', 400, 500)

cv2.namedWindow('Equalized Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Equalized Image', 400, 500)

cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
