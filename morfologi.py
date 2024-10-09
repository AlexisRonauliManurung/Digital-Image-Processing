import cv2

img = cv2.imread('foto alexis.jpg', cv2.IMREAD_REDUCED_COLOR_4)
operasi = 0
while operasi < 1 or operasi > 4:
    print("1. Erosi\n2. Dilasi\n3. Opening\n4. Closing")
    operasi = int(input("Pilih operasi morfologi pada citra (1-4): "))

if operasi == 1:
    new_img = cv2.erode(img, None)
elif operasi == 2:
    new_img = cv2.dilate(img, None)
elif operasi == 3:
    new_img = cv2.erode(img, None)
    new_img = cv2.dilate(new_img, None)
else: 
    new_img = cv2.dilate(img, None)
    new_img = cv2.erode(new_img, None)

cv2.imshow('normal', img)
cv2.imshow('citra baru', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
