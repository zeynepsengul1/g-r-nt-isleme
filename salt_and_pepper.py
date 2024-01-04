import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_salt_and_pepper_noise(image_path, salt_prob, pepper_prob):

    img = cv2.imread(image_path)


    noisy_img = img.copy()
    total_pixels = img.size


    num_salt = np.ceil(salt_prob * total_pixels)
    salt_coords = [np.random.randint(0, i - 1, int(num_salt)) for i in img.shape]
    noisy_img[salt_coords[0], salt_coords[1], :] = 255


    num_pepper = np.ceil(pepper_prob * total_pixels)
    pepper_coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in img.shape]
    noisy_img[pepper_coords[0], pepper_coords[1], :] = 0


    plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Orijinal Görüntü'), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(cv2.cvtColor(noisy_img.astype('uint8'), cv2.COLOR_BGR2RGB))
    plt.title('Salt ve Pepper Gürültülü Görüntü'), plt.xticks([]), plt.yticks([])

    plt.show()


image_path = 'C:/Users/Zeynep/images/first_image.jpg'
salt_prob = 0.1
pepper_prob = 0.1
add_salt_and_pepper_noise(image_path, salt_prob, pepper_prob)