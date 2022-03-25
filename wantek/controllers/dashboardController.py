from flask import render_template, url_for, request, session, flash, redirect
from wantek import app
from wantek.controllers.validateLogin import validate_login
from wantek.models.respon import *

@app.route("/dashboard", methods=["GET"])
@validate_login
def dashboard():
    return render_template("dashboard.html", menu="Dashboard")