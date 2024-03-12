import sys
import cv2
import numpy as np
from testes_4 import make_art

def get_resized_image_shape(image):
    height, width = image.shape
    new_width, new_height = int(width / 20), int(height / 40)
    resized_img = cv2.resize(image, (new_width, new_height))

    return resized_img

def test_print_out_ascii():
    make_art.print_out_ascii([
        [0,1,2,3,0,1,2,3],
        [3,2,1,0,3,2,1,0]
    ])

def test_img_to_ascii():
    image = cv2.imread("./tests/jerma.png", 0)

    new_img = get_resized_image_shape(image)

    output = make_art.img_to_ascii(image)

    assert output.shape == new_img.shape

print("batata")

test_print_out_ascii()