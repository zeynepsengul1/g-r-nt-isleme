import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplace_blur(image_path):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    laplace_filter = np.array([[0, 1, 0],
                               [1, -4, 1],
                               [0, 1, 0]])


    laplace_result = cv2.filter2D(img, cv2.CV_64F, laplace_filter)


    plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(laplace_result, cmap='gray')
    plt.title('Laplace Filtre Uygulanmış Görüntü'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/first_image.jpg'
laplace_blur(image_path)