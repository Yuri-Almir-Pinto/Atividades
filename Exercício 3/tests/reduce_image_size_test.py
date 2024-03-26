from projects import reduce_image_size as reduce_img
import cv2

def test_resize_image():
    reduce_img_img = reduce_img.resize_image("./artifacts/jerma.png", 50)
    my_rescaled = cv2.imread("./artifacts/rescaled_result.png")

    assert reduce_img_img.all() == my_rescaled.all()
    assert reduce_img_img.shape == my_rescaled.shape