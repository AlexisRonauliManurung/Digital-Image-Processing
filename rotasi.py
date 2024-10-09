import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('foto alexis.jpg', cv.IMREAD_REDUCED_COLOR_4)

# Check if the image is loaded successfully
if img is None:
    print("Error: Unable to load image.")
else:
    # Get the dimensions of the image
    rows, cols, _ = img.shape

    # Define the rotation angle (in degrees)
    angle = 45  # Rotate the image by 45 degrees

    # Define the rotation point (center of the image)
    center = (cols // 2, rows // 2)

    # Create the rotation matrix
    rotation_matrix = cv.getRotationMatrix2D(center, angle, 1.0)

    # Apply the rotation using warpAffine
    rotated_img = cv.warpAffine(img, rotation_matrix, (cols, rows))

    # Display the original and rotated images
    cv.imshow('Original Image', img)
    cv.imshow('Rotated Image', rotated_img)

    # Wait for a key press and then close the windows
    cv.waitKey(0)
    cv.destroyAllWindows()
