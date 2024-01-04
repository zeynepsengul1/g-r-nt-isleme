import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_esitleme(image_path):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    equ = cv2.equalizeHist(img)


    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.title('Orijinal Histogram'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(equ, cmap='gray')
    plt.title('Eşleştirilmiş Görüntü'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.hist(equ.flatten(), 256, [0, 256], color='r')
    plt.title('Eşleştirilmiş Histogram'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/second_image.jpg'
histogram_esitleme(image_path)