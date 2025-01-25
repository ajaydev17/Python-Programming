"""
A session in Flask is a way to store data across multiple requests for a specific user.
Flask sessions are client-side, meaning the session data is stored in a cookie on the user's
browser, signed cryptographically to prevent tampering. Each user gets a unique session
cookie, and Flask uses this cookie to keep track of data for that specific user between
different requests.

Flask provides a session object, which allows developers to store and retrieve session data.
This data is accessible only for the duration of the session, which lasts until the user closes the
browser or the session expires.
"""

from flask import Flask, session, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route('/')
def home():
    if 'username' in session:
        return f'Logged in as {session["username"]}'


@app.route('/login', methods=['POST'])
def login():
    user_name = request.get_json().get('username', None)
    session['username'] = user_name
    return f'Logged in as {user_name}'


@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'Logged out'