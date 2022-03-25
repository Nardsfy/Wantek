import hashlib
from flask import render_template, url_for, request, session, flash, redirect
from wantek import app
from wantek.controllers.validateLogin import validate_login
from wantek.models.respon import *
from wantek.dao.userDAO import *

@app.route("/", methods=["GET"])
@app.route("/login", methods=["GET"])
@validate_login
def login():              
    return render_template("login.html", menu="Login")

@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    session["logged_in"] = False
    return render_template("login.html")

@app.route("/login_post", methods=["POST"])
def loginPost():
    session["logged_in"] = False
    v_username = request.form.get("username")    
    password = request.form.get("password") 
    hashPassword = hashlib.md5(password.encode())
    v_password = hashPassword.hexdigest()   
    dataUser = getUser(v_username, v_password)      
    if dataUser["status"] == "F": # if error from dao select data user
        flash(dataUser["message"], "error")
        return redirect(url_for("login"))
    else:              
        if dataUser["result"]: # make sure user credentials match with database user           
            session["username"] = dataUser["result"][0]["username"]        
            session["roles"] = dataUser["result"][0]["roles"]    
            session["logged_in"] = True
            return redirect(url_for("dashboard"))
        else:
            flash(dataUser["message"], "error")
            return redirect(url_for("login"))