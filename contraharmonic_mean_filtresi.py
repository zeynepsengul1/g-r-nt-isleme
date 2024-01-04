import cv2
import numpy as np
import matplotlib.pyplot as plt

def contraharmonic_mean_filter(image_path, kernel_size, Q):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    kernel = np.ones((kernel_size, kernel_size), np.uint8)


    noisy_img = img + np.random.normal(0, 25, img.shape).astype(np.uint8)


    filtered_img = cv2.filter2D(noisy_img, -1, kernel)


    plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(noisy_img, cmap='gray')
    plt.title('Gürültülü Görüntü'), plt.xticks([]), plt.yticks([])

    plt.show()

    plt.subplot(1, 2, 1), plt.imshow(filtered_img, cmap='gray')
    plt.title('Contraharmonic Mean Filtreleme'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/first_image.jpg'
kernel_size = 3
Q = 1.5
contraharmonic_mean_filter(image_path, kernel_size, Q)