import cv2

# Baca citra dari file
image_path = 'foto alexis.jpg'
image = cv2.imread(image_path, cv2.IMREAD_REDUCED_COLOR_2)

# Periksa apakah citra berhasil dibaca
if image is None:
    print("Gagal membaca citra.")
else:
    # Tampilkan citra
    cv2.imshow('Citra', image)
    cv2.waitKey(0)  # Tunggu hingga pengguna menekan tombol apa pun
    cv2.destroyAllWindows()  # Tutup semua jendela OpenCV

