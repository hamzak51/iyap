from flask import Flask, render_template, request, session   # flask modules

import requests
from datetime import datetime   # python modules

import os
from dotenv import load_dotenv  # env modules

from flask_sqlalchemy import SQLAlchemy # db modules

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:password@localhost/yap"
db = SQLAlchemy(app)


class blogs(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    tagline = db.Column(db.String, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.String, nullable=False)
    picture_path = db.Column(db.String, nullable=False)


@app.route("/")
def blog():
    return render_template("blog.html")


@app.route("/dashboard", methods=['POST', 'GET'])
def dashboard():
    #Check if admin logged in
    # if ('admin' in session and session['admin'] == admin_user):
    if 'admin' in session:
        return render_template("dashboard.html")
    #if loggen_in:
    if request.method=='POST':

        # getting values from the form
        username = request.form.get("username")
        password = request.form.get("password")

        # admin credentials from .env
        admin_user=os.getenv("admin_user")
        admin_pass=os.getenv("admin_pass")

        if (admin_user==username and admin_pass==password):
            session['admin'] = username
            return render_template("dashboard.html") 
    #show dashboard
        else:
            return render_template("login.html", error="Only admins are allowed to access dashboard")
    #else:
    #show login form
    return render_template("login.html")


# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000)) 
#     app.run(host="0.0.0.0", port=port, debug=True)


app.run (debug=True)