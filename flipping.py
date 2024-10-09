import cv2

#Load citra asli
original_image = cv2.imread('foto alexis.jpg', cv2.IMREAD_REDUCED_COLOR_4)

#Flipping Horizontal
horizontal_flipped_image = cv2.flip(original_image, 1)

#Flipping Vertical
vertical_flipped_image = cv2.flip(original_image, 0)

#Menampilkan citra-citra hasil flipping
cv2.imshow('Original Image', original_image)
cv2.imshow('Horizontal Flipped Image', horizontal_flipped_image)
cv2.imshow('Vertical Flipped Image', vertical_flipped_image)

#Menunggu sampai jendela citra ditutup
cv2.waitKey(0)
cv2.destroyAllWindows()
