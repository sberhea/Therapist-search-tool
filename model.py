"""Models for therapist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from datetime import datetime 

# Replace this with your code!
class User(db.Model):
    """A user."""

    __tablename__ = 'user'

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
    name = db.Column(db.String)
    # specialty = db.Column(db.String)
    # address = db.Column(db.Text)
    pic = db.Column(db.String)
    description = db.Column(db.Text)
    longitude = db.Column(db.Numeric(precision=20, 
                        scale=15), 
                        nullable=False)
    latitude = db.Column(db.Numeric(precision=20, 
                        scale=15), 
                        nullable=False)
    # therapist_email = db.Column(db.String)
    phonenum  = db.Column(db.String)
    fp = db.Column(db.String)
    sliding_scale = db.Column(db.String)

    # Bookmark = list of bookmarks. One_bookmark = one individual bookmark. 

    # bookmark = db.relationship("Bookmark",
    #                         #  secondary="one_bookmark",
    #                          backref="therapist")

class Insurance(db.Model):

    __tablename__ = 'insurance'

    insurance_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    company_name = db.Column(db.String)
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapist.therapist_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
        
    user = db.relationship('User', backref='insurance')
    therapist = db.relationship('Therapist', backref='insurance')
 
    def __repr__(self):
        return f'<Insurance insurance_id={self.insurance_id} company_name={self.company_name}>'

class Bookmark(db.Model):
    """A list of therapists the user bookmarked"""
    
    __tablename__ = 'bookmark'

    bookmark_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapist.therapist_id'))
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    
    user = db.relationship('User', backref='bookmarks') # look nto the secondary syntax (see data modeling lecture, BookGenres)
    therapist = db.relationship('Therapist', backref='bookmarks')

# class OneBookmark(db.Model):
#     """One bookmarked therapist"""
    
#     __tablename__ = 'one_bookmark'

#     one_bookmark_id = db.Column(db.Integer,
#                             autoincrement=True,
#                             primary_key=True)
#     therapist_id = db.Column(db.Integer, 
#                             db.ForeignKey('therapist.therapist_id'), 
#                             nullable=False)
#     bookmark_id = db.Column(db.Integer, 
#                             db.ForeignKey('bookmark.bookmark_id'), 
#                             nullable=False)
    

def connect_to_db(flask_app, db_uri='postgresql:///therapist', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
