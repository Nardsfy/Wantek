from flask import render_template, url_for, request, session, flash, redirect
from wantek import app
from wantek.controllers.validateLogin import validate_login
from wantek.models.respon import *

@app.route("/master_user", methods=["GET"])
@validate_login
def masterUser():
    return render_template("master/masterUser.html", menu="Master")

@app.route("/master_stock", methods=["GET"])
@validate_login
def masterStock():
    return render_template("master/masterStock.html", menu="Master")