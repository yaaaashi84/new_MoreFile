# requestとredirectのインポート
from flask import Flask, render_template, request, redirect
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from db_config import Customer
from datetime import datetime

import luckynumber
import functions
import idpass


config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 1800,
}

app = Flask(__name__)


# ユーザー追加のルーティング(POSTでアクセス限定)
@app.route("/add", methods=["POST"])
def add_customer():
    """新規顧客を追加する関数"""
    # フォーム入力されたnameとageを値に受け取る
    user_id = request.form["user_id"]
    name = request.form["name"]
    nickname = request.form["nickname"]
    age = request.form["age"]
    birthday = request.form["birthday"]
    birthplace = request.form["birthplace"]
    birthcity = request.form["birthcity"]
    hobby = request.form["hobby"]
    food = request.form["food"]
    book = request.form["book"]
    myword = request.form["myword"]
    color = request.form["color"]
    music = request.form["music"]
    respect_person = request.form["respect_person"]

    # 分割代入でも可
    # [name, age] = request.form

    # 登録処理
    Customer.create(
        user_id=user_id,
        name=name,
        nickname=nickname,
        age=age,
        birthday=birthday,
        birthplace=birthplace,
        birthcity=birthcity,
        hobby=hobby,
        food=food,
        book=book,
        myword=myword,
        color=color,
        music=music,
        respect_person=respect_person,
    )

    # index()にリダイレクトする
    return redirect(f"/{user_id}/choice")


@app.route("/")
def input_profile():
    customers = Customer.select()
    print(customers[0])
    return render_template("index.html")


@app.route("/<user_id>/choice")
def part1(user_id):
    return render_template("choice.html", user_id=user_id)


@app.route("/<user_id>/profile")
def profile(user_id):
    customer = Customer.select().where(Customer.user_id == user_id).get()
    lucky_number = luckynumber.getLuckyNumber(customer.birthday)
    picture = functions.getPicture(customer.birthday)
    return render_template(
        "profile.html",
        name=customer.name,
        lucky_number=lucky_number,
        picture=picture,
    )


@app.route("/<user_id>/idpass", methods=["GET", "POST"])
def get_idpass(user_id):
    if request.method == "POST":
        user_id = request.form["user_id"]
    customer = Customer.select().where(Customer.user_id == user_id).get()
    lucky_number = luckynumber.getLuckyNumber(customer.birthday)
    password = idpass.create_pass(
        customer.name, customer.food, lucky_number
    )
    id = idpass.create_id(customer.name, customer.color, lucky_number)
    return render_template("idpass.html", password=password, id=id)


# @app.route()



if __name__ == "__main__":
    app.run(port=5000, debug=True)