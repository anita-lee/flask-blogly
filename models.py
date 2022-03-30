"""Models for Blogly."""

class User(db.Model):
    """Create User."""

    __tablename__ = 'users'

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
        nullable=True,
        default='No image')

