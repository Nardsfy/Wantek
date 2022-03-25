import psycopg2
from flask import Flask

app = Flask(__name__)
app.secret_key = app.config["SECRET_KEY"]

app.config.from_pyfile('settings.py') #konfigurasi diambil dari file settings.py

def dbConnect():
    ''' Function buat open koneksi Database '''    
    connection = psycopg2.connect(user=app.config["USER"],password=app.config["PASSWORD"],host=app.config["HOST"],port=app.config["PORT"],database=app.config["DATABASE"])
    return connection

from wantek.controllers import (routes)
from wantek.controllers import (loginController, dashboardController)
from wantek.controllers.master import (masterController)
from wantek.controllers.transaction import (transactionController)