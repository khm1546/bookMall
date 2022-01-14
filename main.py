from flask import Flask
from datetime import datetime
from flask import render_template, request, redirect, url_for, session, jsonify
import pymysql
import json


app = Flask(__name__)

@app.route("/")
def index():

    return render_template("/mypage/Cart.html")

@app.route("/buy")
def buy():

    return render_template("/mypage/buy.html")

@app.route("/refund")
def refund():

    return render_template("/mypage/refund.html")

@app.route("/refund-reason")
def reason():

    return render_template("/mypage/refund-reason.html")

@app.route("/refund-success")
def refund_success():

    return render_template("/mypage/refund-success.html")

@app.route("/delivery-insert")
def delivery_insert():

    return render_template("/mypage/delivery-insert.html")

@app.route("/buy-success")
def buy_success():

    return render_template("/mypage/buy-success.html")

@app.route("/buy-list")
def buy_list():

    return render_template("/mypage/buy-list.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

