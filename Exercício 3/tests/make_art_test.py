import cv2
from projects import make_art
from contextlib import redirect_stdout
from io import StringIO

def get_resized_image_shape(image):
    height, width = image.shape
    new_width, new_height = int(width / 20), int(height / 40)
    resized_img = cv2.resize(image, (new_width, new_height))

    return resized_img

def test_print_out_ascii_with_image() -> None:
    compare_ascii: str = ""
    with open('./artifacts/ascii.txt', 'r') as file:
        for line in file:
            compare_ascii += line

    error_image = cv2.imread("./artifacts/error_image.png", 0)

    output = make_art.img_to_ascii(error_image)

    f = StringIO()
    with redirect_stdout(f):
        make_art.print_out_ascii(output)

    assert f.getvalue() == compare_ascii
    

def test_print_out_ascii():
    f = StringIO()
    with redirect_stdout(f):
        make_art.print_out_ascii([
            [0,1,2,3,4,5,0,1,2,3,4,5],
            [5,4,3,2,1,0,5,4,3,2,1,0]
        ])

    assert f.getvalue() == "#-*.+o#-*.+o\no+.*-#o+.*-#\n"

def test_img_format():
    image = cv2.imread("./artifacts/jerma.png", 0)

    new_img = get_resized_image_shape(image)

    output = make_art.img_to_ascii(image)

    assert output.shape == new_img.shape