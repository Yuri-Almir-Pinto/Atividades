from projects import random_password_gen as password

def test_generate_pass():
    password_check = {}
    for i in range(10000):
        gen_password = password.generate_pass(10)
        if gen_password in password_check.keys():
            assert False, "Houve senha repetida."
        else:
            password_check[gen_password] = True
        