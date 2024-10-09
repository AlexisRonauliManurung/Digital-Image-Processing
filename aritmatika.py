import cv2

# Membaca citra
img1 = cv2.imread("foto alexis.jpg", cv2.IMREAD_REDUCED_COLOR_4)
img2 = cv2.imread("foto alexis.jpg", cv2.IMREAD_REDUCED_COLOR_4)

# Menambahkan dua citra
added_img = cv2.add(img1, img2)

# Mengurangkan dua citra
subtracted_img = cv2.subtract(img1, img2)

# Mengkalikan dua citra
multiplied_img = cv2.multiply(img1, img2)

# Membagi dua citra
divided_img = cv2.divide(img1, img2)

# Menampilkan citra hasil operasi aritmetika
cv2.imshow("Added image", added_img)
cv2.imshow("Subtracted image", subtracted_img)
cv2.imshow("Multiplied image", multiplied_img)
cv2.imshow("Divided image", divided_img)

# Menunggu pengguna menutup jendela citra
cv2.waitKey(0)
