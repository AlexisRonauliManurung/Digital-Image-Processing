import cv2
import numpy as np

# Fungsi untuk melakukan zoom pada citra
def zoom_image(image, scale_factor):
    # Dapatkan dimensi citra
    height, width = image.shape[:2]
    
    # Hitung ukuran baru setelah zooming
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)
    
    # Resize citra dengan menggunakan metode INTER_LINEAR
    zoomed_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    
    return zoomed_image

# Baca citra
image = cv2.imread('foto alexis.jpg', cv2.IMREAD_REDUCED_COLOR_4)

# Tentukan faktor zoom
scale_factor = 1.5  # Ganti dengan faktor zoom yang diinginkan

# Panggil fungsi zoom_image
zoomed_image = zoom_image(image, scale_factor)

# Tampilkan citra asli
cv2.imshow('Original Image', image)

# Tampilkan citra setelah zooming
cv2.imshow('Zoomed Image', zoomed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
