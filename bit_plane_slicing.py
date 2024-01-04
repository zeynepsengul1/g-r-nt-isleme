import cv2
import numpy as np

def bit_plane_slice(image_path, bit_level):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    bit_plane = np.bitwise_and(img, 2 ** bit_level)


    cv2.imshow(f'Bit Plane {bit_level}', bit_plane)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



image_path = 'C:/Users/Zeynep/images/first_image.jpg'
bit_level = 7
bit_plane_slice(image_path, bit_level)