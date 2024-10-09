import cv2
import os

# Ganti path gambar sesuai dengan lokasi yang benar
image_path = 'citra negatiff.png'

if os.path.exists(image_path):
    IMG = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if IMG is not None:
        def find_coord(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                color = IMG[y, x]
                print(f"Koordinat (x, y): ({x}, {y}) - Warna pixel (BGR): {color}")
                font = cv2.FONT_HERSHEY_PLAIN
                cv2.putText(IMG, f"({x}, {y})", (x, y), font, 1, (255, 0, 0))
                cv2.imshow('SEHUN', IMG)

        cv2.imshow('SEHUN', IMG)
        cv2.setMouseCallback('SEHUN', find_coord)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Gagal membaca gambar. Pastikan format gambar di {image_path} dapat dibaca oleh OpenCV.")
else:
    print(f"File gambar tidak ditemukan di {image_path}. Pastikan path gambar benar.")

