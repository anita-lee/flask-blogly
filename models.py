
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://picsum.photos/200'

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


"""Models for Blogly."""

class User(db.Model):
    """Create User."""

    __tablename__ = 'users'

    posts = db.relationship('Post', backref='user')

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    first_name = db.Column(
        db.String(50),
        nullable=False)

    last_name = db.Column(
        db.String(50),
        nullable=False)

    image_url = db.Column(
        db.String,
        nullable=False,
        default=DEFAULT_IMAGE_URL)

class Post(db.Model):
    """Create Post."""

    __tablename__ = 'posts'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    title = db.Column(
        db.String(50),
        nullable=False)

    content = db.Column(
        db.Text,
        nullable=False)

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.now())

    user_id = db.Column(
        db.ForeignKey('users.id'),
        nullable=False)


class Tag(db.Model):
    """Creates Tag model"""

    __tablename__ = "tags"

    projects = db.relationship('Post',
                               secondary='post_tags',
                               backref='tags')

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    name = db.Column(
        db.String(20),
        nullable=False)

class PostTag(db.Model):

    __tablename__ = "posts_tags"

    post_id = db.Column(
        db.Integer,
        db.ForeignKey('posts.id'),
        primary_key=True
    )
    tag_id = db.Column(
        db.Integer,
        db.ForeignKey('tags.id'),
        primary_key=True
    )
