import cv2
import numpy as np
import matplotlib.pyplot as plt

def smoothing_and_sharpening(image_path):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    blurred = cv2.GaussianBlur(img, (7, 7), 3)



    laplace_filter = np.array([[0, 1, 0],
                               [1, -4, 1],
                               [0, 1, 0]])

    sharpened = cv2.filter2D(img, cv2.CV_64F, laplace_filter)


    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 2), plt.imshow(blurred, cmap='gray')
    plt.title('Smoothing (Blurring)'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 3, 3), plt.imshow(sharpened, cmap='gray')
    plt.title('Sharpening'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/first_image.jpg'
smoothing_and_sharpening(image_path)