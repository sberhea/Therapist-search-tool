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

@app.route('/user', methods=['POST'])
def create_registration():
    """Create user registration"""
    
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    
    if user:
        flash('Cannot create an account with that email. Try again.')
        return redirect('/')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

        return redirect('/')

# @app.route('/login', methods=['POST'])
# def login():

@app.route('/profile')
def user_profile():
    """This is the user profile"""

@app.route('/search')
def search_tool():
    """Search bar, filter and Google Maps displayed"""

@app.route('/therapists')
def all_therapists():
    """View all therapists."""

    therapist = crud.get_therapist()

    return render_template('all_therapists.html', therapist=therapist)

@app.route('/therapists/<therapist_id>')
def one_therapist():
    """Display one therapist after the user clicks on a listing"""
    
    therapist_details = crud.therapist_details()

    return render_template('therapist_details.html', therapist=therapist)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)