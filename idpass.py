import random
import string
from db_config import Customer
import luckynumber

symbol_list = ["#", "$", "%", "&", "!"]


def create_pass(name, food, lucky_number):
    str1 = name[1]
    str2 = name[-4:-1].upper()
    sym = random.choice(symbol_list)
    str3 = food[1]
    str4 = food[-1:-4]
    num = str(lucky_number)

    pass_list = [str1, sym, str2, str3, str4, num]
    random.shuffle(pass_list)

    password = "".join(pass_list)

    return password


def create_id(name, color, lucky_number):
    str_id = color
    str_name = name[0].upper()
    num_id = str(lucky_number)

    createid = f"{str_id}{str_name}_{num_id}"

    return createid
