# requestとredirectのインポート
from flask import Flask, render_template, request, redirect
from config import Customer

app = Flask(__name__)


@app.route("/index")
def index():
    customers = Customer.select()
    return render_template("index.html", customers=customers)


# ユーザー追加のルーティング(POSTでアクセス限定)
@app.route("/add", methods=["POST"])
def add_customer():
    """新規顧客を追加する関数"""
    # フォーム入力されたnameとageを値に受け取る
    name = request.form["name"]
    age = request.form["age"]
    name = request.form["name"]
    age = request.form["age"]
    name = request.form["name"]
    age = request.form["age"]
    name = request.form["name"]
    age = request.form["age"]
    name = request.form["name"]
    age = request.form["age"]
    name = request.form["name"]
    age = request.form["age"]

    # 分割代入でも可
    # [name, age] = request.form

    # 登録処理
    Customer.create(name=name, age=age)

    # index()にリダイレクトする
    return redirect("/index")


if __name__ == '__main__':
    app.run(port=5000, debug=True)