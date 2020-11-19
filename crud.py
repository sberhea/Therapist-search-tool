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

def login_user():
    username = User.query.get(email)
    password = User.query.get(password) 

def get_user_by_email(email):
    
    return User.query.filter(User.email == email).first()

def verify_user_login(email, password):
    return User.query.filter(User.email == email & User.password == password).first()

def get_user_by_id(user_id):

    return User.query.get(user_id)


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

def get_therapist():
    return Therapist.query.all()
     

def therapist_details(therapist_id):
    return Therapist.query.get(therapist_id)
     

def create_bookmark(user, therapist):
    """Create and return a new bookmark."""

    bookmark = Bookmark(user=user, therapist=therapist)

    db.session.add(bookmark)
    db.session.commit()

    return bookmark

def get_bookmark_by_userid(user_id): #renamethis func if you wan it to both return all bookma=rked theapists AND add a bookmarked traoist
    """Find bookmarks associated with a user id"""
    therapist_list = db.session.query(Bookmarks.therapist_id).filter_by(user_id=user_id).all()
    bookmarks = []
    user = User.query.get(user_id)
    user.therapists.append(this_would_be_aTherapist_object) #if you have t object, this will create the relationship

    for t in therapist_list:
        bookmarks.append(db.session.query(Therapist.name).filter_by(therapist_id=t.therapist_id).all())
    
    return bookmarks

