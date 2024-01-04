import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_filter(image_path, kernel_size, sigma):

    img = cv2.imread(image_path)


    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    kernel_2d = np.outer(kernel, kernel.T)


    img_filtered = cv2.filter2D(img, -1, kernel_2d)


    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(img_filtered, cv2.COLOR_BGR2RGB))
    plt.title(f'Gaussian Filtre (Kernel Boyutu: {kernel_size}, Sigma: {sigma})'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/first_image.jpg'
kernel_size = 20
sigma = 50.0
gaussian_filter(image_path, kernel_size, sigma)