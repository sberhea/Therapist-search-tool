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

@app.route('/login') #method not allowed
def login():
    """Log in user."""
    username = User.query.get(email)
    password = User.query.get(password) 
    
    user = User.get(email=email,
                        password=password).first()
    
    if user:
        login_user(user)
        return render_template('user_profile.html', user=user)
    else:
        flash('Username or password incorrect')
        return render_template('/login')


@app.route('/profile/<user_id>')
def user_profile(user_id):
    """This is the user profile"""
    user = crud.get_user_by_id(user_id)

    session['user.id'] = session.get('user.id', user.id)

    return render_template('user_profile.html', user=user, user_id=user_id)


@app.route('/search')
def search_tool():
    """Search bar, filter and Google Maps displayed"""

@app.route('/therapists')
def all_therapists():
    """View all therapists."""

    therapist = crud.get_therapist()

    return render_template('all_therapists.html', therapist=therapist)

@app.route('/therapists/<therapist_id>')
def one_therapist(therapist_id):
    """Display one therapist after the user clicks on a listing"""
    
    therapist_details = crud.therapist_details(therapist_id)

    return render_template('therapist_details.html', 
                            therapist_details=therapist_details)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)