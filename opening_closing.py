import cv2
import numpy as np
import matplotlib.pyplot as plt

def opening_closing_operations(image_path, kernel_size_opening, kernel_size_closing):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    kernel_opening = np.ones((kernel_size_opening, kernel_size_opening), np.uint8)
    kernel_closing = np.ones((kernel_size_closing, kernel_size_closing), np.uint8)


    opened_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_opening)


    closed_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel_closing)


    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2), plt.imshow(opened_img, cmap='gray')
    plt.title('Açma İşlemi'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 3), plt.imshow(closed_img, cmap='gray')
    plt.title('Kapanma İşlemi'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/first_image.jpg'
kernel_size_opening = 5
kernel_size_closing = 5

opening_closing_operations(image_path, kernel_size_opening, kernel_size_closing)