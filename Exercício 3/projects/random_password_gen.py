import random
import math

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

def _randomize(password, length, array, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)

def generate_pass(pass_len):

    alpha_len = pass_len // 2
    num_len = math.ceil(pass_len * 30 / 100)
    special_len = pass_len - (alpha_len + num_len)

    password = []

    _randomize(password, alpha_len, alpha, True)

    _randomize(password, num_len, num)

    _randomize(password, special_len, special)

    random.shuffle(password)

    gen_password = ""
    for i in password:
        gen_password = gen_password + str(i)

    return gen_password