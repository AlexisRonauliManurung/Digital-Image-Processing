import cv2

IMG = cv2.imread('citra biner.png', cv2.IMREAD_COLOR)

# Convert image to grayscale
gray_image = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)

# Threshold the grayscale image
binary_image = cv2.threshold(gray_image, 128, 1, cv2.THRESH_BINARY)[1]

def find_coord(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        binary_value = binary_image[y, x]  # Get binary value at (x, y)

        print(f"Koordinat (x, y): ({x}, {y}) - Warna pixel (Binary): {binary_value}")

        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(IMG, f"({x}, {y})", (x, y), font, 1, (255, 0, 0))
        cv2.imshow('SEHUN', IMG)

if __name__ == "__main__":
    cv2.imshow('SEHUN', IMG)
    cv2.setMouseCallback('SEHUN', find_coord)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


