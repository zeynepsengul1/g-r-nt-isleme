import cv2
import numpy as np
import matplotlib.pyplot as plt

def average_filter(image_path, kernel_size):

    img = cv2.imread(image_path)


    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)


    img_filtered = cv2.filter2D(img, -1, kernel)


    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(img_filtered, cv2.COLOR_BGR2RGB))
    plt.title(f'Ortalama Filtre (Kernel Boyutu: {kernel_size})'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/first_image.jpg'
kernel_size = 30
average_filter(image_path, kernel_size)