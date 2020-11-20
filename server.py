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

    # session['user.id'] = session.get('user.id', user.id)

    return render_template('login.html')

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.verify_user_login(email, password)
    
    print("***********", user.user_id)

    if user and user.password == password:
        session['user_id'] = user.user_id
        print(user.user_id)
        # flash(f'Login successful! {email}')
        return redirect('/profile')
    else:
        flash('Username or password incorrect')
        return redirect('/login')
    
@app.route('/logout')
def logout_user():
    
    user_id = session.get('user_id')
    user = crud.get_user_by_id(user_id)

    if user:
        del session['user_id']
        return redirect('/')

@app.route('/profile', methods=['POST'])
def user_profile():
    """This is the user profile"""

    user_id = session.get('user_id')
    user = crud.get_user_by_id(user_id)
    
    # session['user_id'] = user.user_id
    # session.get('user_id', user_id)


    return render_template('user_profile.html', user=user, user_id=user_id)

@app.route('/bookmark/<therapist_id>', methods=['POST', 'GET'])
def add_bookmark(therapist_id):
    
    user_id = session.get('user_id')
    user = crud.get_user_by_id(user_id) #uncommented quotes
    
    therapist = crud.therapist_details('therapist_id')
    print(therapist.therapist_id)
    
    if user:
        bookmark = crud.create_user_bookmark(user, therapist_id)
        flash('Bookmark added')
        return redirect('/therapists', user=user, therapist_id=therapist_id)
    else:
        flash('Cannot bookmark therapist')
        return redirect('/therapists')
    

@app.route('/my-bookmarks')
def show_bookmarks():
    
    user_id = session.get('user_id')
    print('********', user_id)
    
    if user_id:
        user = crud.get_user_by_id(user_id)
        bookmarks = crud.get_bookmark_list(user_id)
        
        return render_template('bookmark.html', user=user, bookmarks=bookmarks)
    else:
        flash('You have no bookmarks')
        return redirect('/')
        
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
    
    therapist = crud.therapist_details(therapist_id)

    return render_template('therapist_details.html', 
                            therapist=therapist)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)