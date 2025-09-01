# Personal Blog
A simple blogging platform built with Flask, SQLAlchemy, and MySQL.
Users can browse blog posts, view single post pages, and see suggested articles.

## Features
+ Home page listing all blog posts
+ Single post page with:
    + Featured image
    + Featured image
    + Title, tagline, date, author
    + Post content (rich text supported)
    + Suggested posts section
+ Database powered by MySQL

## Tech Stack
+ **Backend**: Flask (Python)
+ **Database**: MySQL
+ **ORM**: SQLAlchemy
+ **Frontend**: HTML/CSS/JS

## Setup
1. clone repo
```
git clone https://github.com/your-username/flask-blog.git
cd flask-blog
```

2. Create Virtual environment
```
python -m venv env
source env/bin/activate   # macOS/Linux
env\Scripts\activate      # Windows
```

3. Install requirements
```
pip install -r requirements.txt
```

4. Configure Database
```
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://username:password@localhost:5432/blogdb"
```

5. Run locally
```
python app.py
```

> Make sure you have atleast one(1) entry in the database before running the app!

## License
This project is open source under the MIT License.