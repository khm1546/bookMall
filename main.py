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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

