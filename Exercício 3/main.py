from tests import qr_code_generator_test as qr_test, make_art_test as art_test
from tests import reduce_image_size_test as reduce_img_test
from projects import reduce_image_size as reduce_img
from projects import unique_words_in_file as unique_words
from projects import random_password_gen as password

if __name__ == "__main__":
    senha = password.generate_pass(20)

    print(senha)


    