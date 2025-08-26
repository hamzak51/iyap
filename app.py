from flask import Flask, render_template, request
import requests
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
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


@app.route("/dashboard")
def dashboard():
    #Check if admin logged in
    #if loggen_in:
    #show dashboard
    #else:
    #show login form


# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000)) 
#     app.run(host="0.0.0.0", port=port, debug=True)


app.run (debug = True)