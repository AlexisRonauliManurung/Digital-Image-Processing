import cv2

# Membaca gambar
image = cv2.imread("foto alexis.jpg", cv2.IMREAD_REDUCED_COLOR_4)

# Mengubah citra menjadi citra negatif
negative_image = cv2.bitwise_not(image)

# Menampilkan citra asli dan citra negatif
cv2.imshow("Citra Asli", image)
cv2.imshow("Citra Negatif", negative_image)

# Menunggu pengguna untuk menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
