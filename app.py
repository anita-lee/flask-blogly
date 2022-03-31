"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import DEFAULT_IMAGE_URL, db, connect_db, User, Post
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.get("/")
def list_users():
    """List users."""
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
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url'] or None

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.get("/users/<int:user_id>")
def show_user_by_id(user_id):
    """Display user by id."""

    #retrieve data for specified user_id
    #pass data to template.

    user = User.query.get_or_404(user_id)
    print("USER=", user)

    return render_template("user_detail.html", user=user)

@app.get("/users/<int:user_id>/edit")
def show_edit_user(user_id):
    """Display edit user page."""

    #retrieve data for specified user_id
    #pass data to template.
    user = User.query.get_or_404(user_id)

    return render_template("user_edit.html", user=user)

@app.post("/users/<int:user_id>/edit")
def edit_user(user_id):
    """Process edit form, redirect to root"""

    #process edit,
    user = User.query.get_or_404(user_id)

    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url'] or DEFAULT_IMAGE_URL

    db.session.commit()

    return redirect("/")

@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
    """Delete user from db"""

    #"delete" user from db.
    user = User.query.get_or_404(user_id)

    # user.query.delete()
    db.session.delete(user)
    db.session.commit()

    return redirect("/")

@app.get("/users/<int:user_id>/posts/new")
def show_post_form(user_id):
    """Render form to add new post."""

    return render_template("post_new.html")

@app.post("/users/<int:user_id>/posts/new")
def add_post(user_id):
    """Adds new post to db"""

    #retrieve form data here
    title = request.form['title']
    content= request.form['content']

    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{user_id}")

@app.get("/posts/<int:post_id>")
def show_post(post_id):
    """Display post."""

    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    return render_template("post_detail.html", post=post, user=user)

@app.get("/posts/<int:post_id>/edit")
def edit_post(post_id):
    """Display edit post page."""

    post = Post.query.get_or_404(post_id)
    return render_template("post_edit.html", post=post)

@app.post("/posts/<int:post-id]/edit")
