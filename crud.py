"""CRUD operations."""

from model import db, User, Therapist, Bookmark, Insurance, connect_to_db

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime 

if __name__ == '__main__':
    from server import app
    connect_to_db(app)

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_therapist(name, pic, description, phonenum, fp, latitude, longitude, sliding_scale):
    """Create and return a new therapist."""

    therapist = Therapist(name = name,
                    pic=pic,
                    description=description,
                    phonenum=phonenum,
                    fp=fp,
                    latitude=latitude,
                    longitude=longitude,
                    sliding_scale=sliding_scale,)

    db.session.add(therapist)
    db.session.commit()

    return therapist

def create_bookmark(user, therapist, score):
    """Create and return a new rating."""

    bookmark = Bookmark(user=user, therapist=therapist)

    db.session.add(bookmark)
    db.session.commit()

    return bookmark