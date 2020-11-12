"""Server for therapists app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home_page():
    """This is the home page"""

    return render_template('homepage.html')

@app.route('/login')
def login():
    """Where the user logs in"""

@app.route('/profile')
def user_profile():
    """This is the user profile"""

@app.route('/search')
def search_tool():
    """Search bar, filter and Google Maps displayed"""

@app.route('/therapists')
def all_therapist():
    """View all therapists."""

    therapist = crud.get_therapist()

    return render_template('all_therapists.html', therapist=therapist)

@app.route('/one-therapist')
def one_therapist():
    """Display one therapist after the user clicks on a listing"""



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)