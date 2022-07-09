import random
import string
from db_config import Customer
import luckynumber

symbol_list = ["#", "$", "%", "&", "!"]
lucky_number = luckynumber.lucky_number


def create_pass():
    str1 =  # 文字列いっこめ
    sym = random.symbol_list
    str2 =  # 文字列にこめ
    num1 = random.number

    str3 = str2のどこかを大文字にする

    password = str1, sym, str3, num1をランダム配列する

    return password

print(f"パスワードを生成しました【{password}】")


def create_id():
    str_id = # 文字列
    underbar = # 何個アンダーバー入れるか
    num_id = # 誕生日かラッキーナンバー

    createid = f"{str_id}{underbar}{num_id}"

    return createid

print(f"IDを生成しました【{createid}】")