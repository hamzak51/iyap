from flask import Flask, render_template, request, session, redirect, url_for, flash   # flask modules
from flask_ckeditor import CKEditor

import requests
from datetime import datetime   # python modules

import os
from dotenv import load_dotenv  # env modules

from flask_sqlalchemy import SQLAlchemy # db modules

load_dotenv()

app = Flask(__name__)


ckeditor = CKEditor(app)
app.secret_key = os.getenv("secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/yap"
db = SQLAlchemy(app)


class blogs(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    tagline = db.Column(db.String, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.String, nullable=False)
    picture_path = db.Column(db.String, nullable=True)


# GET (fetching all items from database)
def get_posts():
    all_blogs = db.session.execute(db.select(blogs).order_by(blogs.sno)).scalars()
    return all_blogs


# home page (publicly visible)
@app.route("/")
def blog():
    return render_template("blog.html")


# dashboard (visible only to admin-hamza)
@app.route("/dashboard", methods=['POST', 'GET'])
def dashboard():
    if 'admin' in session:
        all_blogs=get_posts()
        return render_template("dashboard.html", role="admin", posts=all_blogs)

    if request.method=='POST':
        # getting values from the form
        username = request.form.get("username")
        password = request.form.get("password")

        # admin credentials from .env
        admin_user=os.getenv("admin_user")
        admin_pass=os.getenv("admin_pass")

        if (admin_user==username and admin_pass==password):
            session['admin'] = username
            all_blogs=get_posts()
            return render_template("dashboard.html", role="admin", posts=all_blogs) 
        else:
            return render_template("login.html", error="Only admins are allowed to access dashboard")

    return render_template("login.html")


# logout from dashboard
@app.route("/logout")
def logout():
    session.pop('admin')
    return redirect("/dashboard")



# POST (adding items to database)
@app.route("/newpost", methods=['POST', 'GET'])
def addpost():

    if 'admin' in session:

        if request.method=='POST':
            title = request.form.get("title")
            tagline = request.form.get("tagline")
            content = request.form.get("ckeditor")

            img = request.files["img"]      # get image uploaded image details
            img_path = os.path.join('static/images', img.filename)  # define save path
            img.save(img_path)  # save image to path(static/images)

            picture_path=f"/static/images/{img.filename}"    # define a web path to display in jinja

            new_post = blogs(title=title, tagline=tagline, content=content, picture_path=picture_path)
            db.session.add(new_post)
            db.session.commit()

            return redirect(url_for("post", post_id=new_post.sno))
        return render_template("addpost.html", role="admin")

    else:
        return redirect("/dashboard")


# GET by id
@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = blogs.query.get(post_id)     # saves entire row data of that id in variable(post)
    return render_template("post.html", post=post)


# PUT (edit existing data in database)
@app.route("/edit/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):

    if 'admin' in session:
        post = blogs.query.get(post_id)

        if request.method=='POST':      # agar iss endpoint me request maari hai tw
                post.title = request.form.get("title")      # post.title ko form ke data se replace krdo
                post.tagline = request.form.get("tagline")  
                post.content = request.form.get("ckeditor")

                db.session.commit()

                return redirect(url_for('post', post_id=post.sno))

        return render_template('editpost.html', post=post)

    else:
        return redirect("/dashboard")



# DELETE (delete data from database)
@app.route("/delete/<int:post_id>", methods=['GET', 'POST'])
def delete_post(post_id):

    if 'admin' in session:
        post = blogs.query.get(post_id)

        db.session.delete(post)
        db.session.commit()
            # flash('blog deleted')
        flashmsg="post deleted"
        return redirect("/dashboard")
    else:
        return redirect("/dashboard")




# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000)) 
#     app.run(host="0.0.0.0", port=port, debug=True)


app.run (debug=True)