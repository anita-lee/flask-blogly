"""Blogly application."""

from flask import Flask
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# RESPONSES_KEY = "responses"
# app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)



connect_db(app)
db.create_all()

@app.get("/")
def list_users():
    """List users and show add form."""

    users = User.query.all()
    return render_template("list.html", users=users)