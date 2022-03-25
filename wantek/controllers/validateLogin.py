import os
from flask import session, render_template, url_for, redirect, flash
from functools import wraps

def validate_login(f):
    @wraps(f)
    def wrap(*args, **kwargs):                       
        if not session.get("logged_in"): # if user not logged in pass to login.html            
            return render_template("login.html", menu="Login")
        elif f.__name__ == "login": # if user try to access login page after logged in
            return redirect(url_for("dashboard"))            
        elif (f.__code__.co_filename).split("\\")[-2] == "master": # get path controller master folder to make sure only admin roles can access
            if session.get("roles") != "admin":
                flash("You have no permission.", "error")                              
                return redirect(url_for("dashboard"))  
            else:
                return f(*args, **kwargs)
        else:            
            return f(*args, **kwargs)
    return wrap
    