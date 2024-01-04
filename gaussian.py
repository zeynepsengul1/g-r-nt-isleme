import cv2
import matplotlib.pyplot as plt

def apply_gaussian_blur(image_path):

    img = cv2.imread(image_path)


    blurred = cv2.GaussianBlur(img, (7,7), 3)


    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
    plt.title(f'Gaussian Filtre (Kernel Boyutu: 5,5)'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/first_image.jpg'

apply_gaussian_blur(image_path)