import cv2
import numpy as np
import matplotlib.pyplot as plt

def gamma_correction(image_path, gamma):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    img_corrected = np.power(img / 255.0, gamma)
    img_corrected = (img_corrected * 255).astype(np.uint8)


    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.title('Orijinal Histogram'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(img_corrected, cmap='gray')
    plt.title(f'Gamma Düzeltme (Gamma={gamma})'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 4), plt.hist(img_corrected.flatten(), 256, [0, 256], color='r')
    plt.title('Düzeltildikten Sonraki Histogram'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/first_image.jpg'
gamma_value = 1.5
gamma_correction(image_path, gamma_value)