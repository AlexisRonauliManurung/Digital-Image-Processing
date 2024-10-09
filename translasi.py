import numpy as np
import cv2 as cv

# Load the image
img = cv.imread('foto alexis.jpg', cv.IMREAD_REDUCED_COLOR_4)

# Check if the image is loaded successfully
if img is None:
    print("Error: Unable to load image.")
else:
    # Get the dimensions of the image
    rows, cols, _ = img.shape

    # Define the translation matrix
    M = np.float32([[1, 0, 100], [0, 1, 50]])

    # Apply the translation using warpAffine
    dst = cv.warpAffine(img, M, (cols, rows))

    # Display the original and translated images
    cv.imshow('Original Image', img)
    cv.imshow('Translated Image', dst)

    # Wait for a key press and then close the windows
    cv.waitKey(0)
    cv.destroyAllWindows()
