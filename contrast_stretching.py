import cv2
import numpy as np
import matplotlib.pyplot as plt

def contrast_stretching(image_path, a, b):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    img_stretched = np.clip((img - a) * (255 / (b - a)), 0, 255).astype(np.uint8)


    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.title('Orijinal Histogram'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(img_stretched, cmap='gray')
    plt.title('Contrast Stretched Görüntü'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.hist(img_stretched.flatten(), 256, [0, 256], color='r')
    plt.title('Contrast Stretched Histogram'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/first_image.jpg'
a, b = 50, 200
contrast_stretching(image_path, a, b)