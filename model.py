"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from datetime import datetime 

# Replace this with your code!
class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)


    # def __repr__(self):
    #     return f'<User user_id={self.user_id} email={self.email}>'

class Therapist(db.Model):
    """A therapist."""

    __tablename__ = 'therapist'

    therapist_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    specialty = db.Column(db.String)
    address = db.Column(db.Text)
    longitude = db.Column(db.float8)
    latitude = db.Column(db.float8)
    therapist_email = db.Column(db.String)
    phone_number  = db.Column(db.String)
    sliding_scale = db.Column(db.Boolean)

    # insurance = a list of Insurance objects

    # def __repr__(self):
    #     return f'<Movie movie_id>{self.movie_id} title={self.title}>'

class Insurance(db.Model):

    __tablename__ = 'insurance'

    insurance_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    company_name = db.Column(db.String)
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapist.therapist_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
        
    user = db.relationship('User', backref='insurance')
    therapist = db.relationship('Therapist', backref='insurance')
 
    # def __repr__(self):
    #     return f'<Rating rating_id={self.rating_id} score={self.score}>'

class Bookmark(db.Model):
"""A list of therapists the user bookmarked"""
    __tablename__ = 'bookmark'

    bookmark_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    
    user = db.relationship('User', backref='bookmark')
    therapist = db.relationship('Therapist', backref='bookmark')

# def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
#     flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#     flask_app.config['SQLALCHEMY_ECHO'] = echo
#     flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db.app = flask_app
#     db.init_app(flask_app)

#     print('Connected to the db!')


# if __name__ == '__main__':
#     from server import app

#     # Call connect_to_db(app, echo=False) if your program output gets
#     # too annoying; this will tell SQLAlchemy not to print out every
#     # query it executes.

#     connect_to_db(app)
