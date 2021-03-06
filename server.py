"""Server for therapists app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
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


""" ********************************* User creation, profile, and log in ********************************* """

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

@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/login', methods=['POST']) #method not allowed
def login_user():
    """Log in user."""

    # session['user.id'] = session.get('user.id', user.id)

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    

    if user and user.password == password:
        session['user_id'] = user.user_id
        print(user.user_id)
        # flash(f'Login successful! {email}')
        return redirect('/profile')
    else:
        flash('Username or password incorrect')
        return redirect('/login')
    
@app.route('/logout', methods=['POST'])
def logout_user():
    
    user_id = session.get('user_id')
    user = crud.get_user_by_id(user_id)

    if user:
        del session['user_id']
        return redirect('/')

@app.route('/profile')
def user_profile():
    """This is the user profile"""
    
    user_id = session.get('user_id')
    bookmark_list = crud.get_bookmark_list(user_id)

    if user_id:
        user = crud.get_user_by_id(user_id)
        return render_template('user_profile.html', user=user, user_id=user_id, bookmark_list=bookmark_list)
    else:
        flash('Please log in')
        return redirect('/login')

""" ********************************* Bookmark routes ********************************* """

@app.route('/bookmark', methods=['POST', 'GET']) 
def add_bookmark():
    
    therapist_id = request.args.get("therapist")
    therapist = crud.get_therapist_byid(therapist_id)

    user_id = session.get('user_id')
    user = crud.get_user_by_id(user_id) #uncommented quotes

    # if therapist_id in Bookmark:
    #     flash('Bookmark already added')
    # else:
    if user:
        bookmark = crud.create_user_bookmark(user, therapist)
        flash('Bookmark added!')
    else:
        flash('Log in to add a bookmark.')
    
    return redirect('/therapists')


@app.route('/my-bookmarks/<user_id>', methods=['GET'])
def show_bookmarks(user_id):
    """Display therapists bookmarked by user"""

    user_id = session.get('user_id')
    print('********', user_id)

    if user_id:
        bookmark_list = crud.get_bookmark_list(user_id)
        
        return render_template("bookmark.html", bookmark_list=bookmark_list)
    else:
        flash('You have no bookmarks')
        return redirect('/')

@app.route('/delete-bookmark')
def delete_bookmark():
    """Deletes bookmark from user profile"""

    user_id = session.get('user_id')
    bookmarks = crud.get_bookmark_list(user_id)

    bookmark_id = crud.get_bookmark_byid(bookmark_id)


""" ********************************* Google Maps routes ********************************* """
@app.route("/map")
def show_map():
    """Show map."""
    
    return render_template('map.html')

@app.route('/api/therapists')
def therapist_info():
    """JSON info about therapists"""

    # therapist_by_id = crud.get_therapist_byid(therapist_id)

    therapists = [
        {
            "therapist_id": therapist.therapist_id,
            "name": therapist.name,
            "pic": therapist.pic,
            "phonenum": therapist.phonenum,
            "description": therapist.description,
            "fp": therapist.fp,
            "latitude": str(therapist.latitude),
            "longitude": str(therapist.longitude)
        }
        for therapist in crud.get_therapist()
    ]

    return jsonify(therapists)

@app.route('/data-vis')
def show_datavis():
    """Stats on Black mental health in MN"""

""" ********************************* Display therapist info ********************************* """
@app.route('/therapists')
def all_therapists():
    """View all therapists."""

    therapist = crud.get_therapist()

    return render_template('all_therapists.html', therapist=therapist)

@app.route('/therapists/<therapist_id>')
def one_therapist(therapist_id):
    """Display one therapist after the user clicks on a listing"""
    
    therapist = crud.get_therapist_byid(therapist_id)

    return render_template('therapist_details.html', 
                            therapist=therapist)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)