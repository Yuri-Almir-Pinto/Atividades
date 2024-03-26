# import openCV library for image handling
import cv2

# read image to be resized by imread() function of openCV library
def resize_image(file_name: str, ratio: int):
    img = cv2.imread(file_name)
    #print(img.shape)

    # set the ratio of resized image
    k = ratio
    width = int((img.shape[1])/k)
    height = int((img.shape[0])/k)

    # resize the image by resize() function of openCV library
    scaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    #print(scaled.shape)

    # show the resized image using imshow() function of openCV library
    #cv2.imshow("Output", scaled)
    #cv2.waitKey(500)
    #cv2.destroyAllWindows()

    # get the resized image output by imwrite() function of openCV library

    return scaled
    
def create_file_from_img(img_name_path:str , img: cv2.Mat) -> None:
    cv2.imwrite(img_name_path, img)