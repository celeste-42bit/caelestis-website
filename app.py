# ------------------------------------------
# caelestis-website
# app.py V.: 0.0.1
# https://github.com/celeste-42bit/caelestis-website
# Copyright (C) 2023 celeste-42bit : MIT
# ------------------------------------------

from flask import Flask
from flask import render_template, request
from os import path, listdir
import login_service

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./uploads"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def index_login():
    usr = request.form["uname"]
    passwd = request.form["passwd"]
    login_service.authenticate(usr, passwd)
    return "200"  # TODO return #t/#f for user found/missing

@app.route("/menu", methods=['POST'])
def menu():
    return render_template("menu.html")

if __name__ == "__main__":
    # active mode
    #app.run(host='0.0.0.0', port=80, debug=False)
    # debug mode
    app.run(debug=True)
