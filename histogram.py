import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('foto alexis.jpg', 0 )
histogram = cv.calcHist([image], [0], None, [256], [0,256])

plt.subplot(1,2,1)
plt.imshow(image)
plt.title('Citra')

plt.subplot(1,2,2)
plt.plot(histogram)
plt.title('Histogram Citra')
plt.xlabel('Nilai Piksel')
plt.ylabel('Frekuensi')
plt.show()
