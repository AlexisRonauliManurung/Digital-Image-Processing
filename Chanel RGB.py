import cv2 as cv #mengimpor library OpenCV dan memberinya alias 'cv' untuk memudahkan penggunaan
import numpy as np #mengimpor library NumPy sebagai np digunakan untuk menghasilkan matriks dengan nilai nol yang digunakan dalam pembuatan saluran warna tunggal

image = cv.imread('foto ayang sehun.jpeg') #membaca gambar 'foto ayang sehun.jpeg' dan menyimpannya dalam variabel 'image'
b, g, r = cv.split(image) #memisahkan gambar ke dalam tiga saluran warna: biru (blue), hijau (green), dan merah (red)
zeros = np.zeros(image.shape[:2], dtype="uint8") #membuat matriks berukuran yang sama dengan gambar yang berisi nilai nol (hitam) untuk semua saluran warna.
#`dtype="uint8"` mengindikasikan bahwa tipe data matriks adalah unsigned 8-bit integer

cv.imshow('NORMAL', image) #menampilkan gambar asli dalam jendela yang diberi judul 'NORMAL'
cv.imshow('RED', cv.merge([zeros, zeros, r])) #menggabungkan saluran merah (R) dari gambar asli dengan matriks nol untuk saluran biru (B) dan hijau (G), sehingga hanya red chanel yang terlihat
cv.imshow('GREEN', cv.merge([zeros, g, zeros])) #menggabungkan saluran hijau (G) dari gambar asli dengan matriks nol untuk saluran biru (B) dan merah (R), sehingga hanya green chanel yang terlihat
cv.imshow('BLUE', cv.merge([b, zeros, zeros])) #Ini menggabungkan saluran biru (B) dari gambar asli dengan matriks nol untuk saluran hijau (G) dan merah (R), sehingga hanya blue chanel yang terlihat
cv.waitKey(0) #program akan menunggu hingga 0 ditekan pada keyboard sebelum melanjutkan
cv.destroyAllWindows() #etelah jendela gambar ditutup, perintah ini akan menghancurkan semua jendela yang dibuat oleh OpenCV
