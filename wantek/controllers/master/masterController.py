import hashlib
from flask import render_template, url_for, request, session, flash, redirect
from wantek import app
from wantek.controllers.validateLogin import validate_login
from wantek.models.respon import *
from wantek.dao.master.masterDAO import *

@app.route("/master_user", methods=["GET"])
@validate_login
def masterUser():
    dataUser = getUser()
    if dataUser["status"] == "F":
        flash(dataUser["message"], 'error')
        return redirect(url_for("masterUser"))
    else:                        
        allUserData = dataUser["result"]        
        return render_template("master/masterUser.html", menu="Master user", data=allUserData)

@app.route("/master_stock", methods=["GET"])
@validate_login
def masterStock():
    return render_template("master/masterStock.html", menu="Master stock")

@app.route("/add_user", methods=["POST"])
@validate_login
def addUser():
    v_username = request.form.get("username")
    password = request.form.get("password")
    v_role = request.form.get("role")
    hashPassword = hashlib.md5(password.encode())
    v_password = hashPassword.hexdigest()        
    resultInsertUser = insertUser(v_username, v_password, v_role)
    if resultInsertUser["status"] == "F": # if error from dao insert new user
        flash(resultInsertUser["message"], 'error')
        return redirect(url_for("masterUser"))
    else:
        flash(resultInsertUser["message"], 'success')
        return redirect(url_for("masterUser"))    