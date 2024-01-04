import cv2
import numpy as np
import matplotlib.pyplot as plt

def rgb_thresholding(image_path, red_threshold, green_threshold, blue_threshold):

    img = cv2.imread(image_path)


    blue_channel, green_channel, red_channel = cv2.split(img)


    blue_mask = (blue_channel < blue_threshold).astype(np.uint8) * 255
    green_mask = (green_channel < green_threshold).astype(np.uint8) * 255
    red_mask = (red_channel < red_threshold).astype(np.uint8) * 255


    result = cv2.bitwise_and(img, img, mask=blue_mask & green_mask & red_mask)


    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title('RGB Bölütlenmiş Görüntü'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/first_image.jpg'
red_threshold = 100
green_threshold = 80
blue_threshold = 60
rgb_thresholding(image_path, red_threshold, green_threshold, blue_threshold)