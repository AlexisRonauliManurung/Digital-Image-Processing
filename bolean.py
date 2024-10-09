import cv2
import numpy as np

img = cv2.imread('foto alexis.jpg', cv2.IMREAD_REDUCED_GRAYSCALE_4)
print("1. Not\n2. Or\n3. And")
operasi = int(input("Pilih operasi boolean pada citra (1-3): "))
while operasi < 1 or operasi > 3:
    print("Ulang")
    operasi = int(input("Pilih operasi boolean pada citra (1-3): "))
new_img = np.zeros((len(img), len(img[0])))

if operasi == 1:
    for i in range(len(img)):
        for j in range(len(img[0])):
            new_img[i,j] = ~img[i,j]
elif operasi == 2:
    disjungsi = int(input("Masukkan skala or (int): "))
    for i in range(len(img)):
        for j in range(len(img[0])):
            new_img[i,j] = img[i,j]|disjungsi
else:
    konjungsi = int(input("Masukkan skala and (int): "))
    for i in range(len(img)):
        for j in range(len(img[0])):
            new_img[i,j] = img[i,j]&konjungsi

new_img = np.clip(new_img, 0, 255)
new_img = new_img.astype(np.uint8)
cv2.imshow('normal', img)
cv2.imshow('cita baru', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
