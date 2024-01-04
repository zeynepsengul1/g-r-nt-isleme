import cv2
import numpy as np
import matplotlib.pyplot as plt

def sobel_filter(image_path):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)


    magnitude = np.sqrt(sobelx**2 + sobely**2)
    orientation = np.arctan2(sobely, sobelx)


    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel Filtre (X Yönü)'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Filtre (Y Yönü)'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 4), plt.imshow(magnitude, cmap='gray')
    plt.title('Kenar Büyüklüğü'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/first_image.jpg'
sobel_filter(image_path)