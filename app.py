"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# RESPONSES_KEY = "responses"
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.get("/")
def list_users():
    """List users and show add form."""


    return redirect("/users")

@app.get("/users")
def show_users():
    """show list of users"""

    users = User.query.all()

    return render_template("index.html", users=users)

@app.get("/users/new")
def show_new_user_form():
    """Render form to add new user."""

    return render_template("user_new.html")

@app.post("/users/new")
def add_new_user():
    """Adds new User to db"""

    #retrieve form data here

    return redirect("/")

app.get("/user/<user_id>")
def show_user_by_id(user_id):
    """Display user by id."""

    #retrieve data for specified user_id
    #pass data to template.

    return render_template("user_detail.html")

app.get("/user/<user_id>/edit")
def show_edit_user(user_id):
    """Display edit user page."""

    #retrieve data for specified user_id
    #pass data to template.

    return render_template("user_edit.html")

app.post("/users/<user_id>/edit")
def edit_user(user_id):
    """Process edit form, redirect to root"""

    #process edit,

    return redirect("/")

app.post("/user/<user_id>/delete")
def delete_user(user_id):
    """Delete user from db"""

    #"delete" user from db.

    return redirect("/")
