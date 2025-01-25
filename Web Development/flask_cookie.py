"""
A cookie is a small piece of data stored on the user's browser, sent back and forth
between the client and server with each request. In Flask, cookies are used to store
information such as user preferences or authentication tokens. Unlike sessions, which are
used to store server-side data accessible only during the session, cookies are client-side and
persist even after the session ends (based on their expiration time).

Flask allows setting cookies through the set_cookie() method on the response object.
Cookies are suitable for small, non-sensitive data, whereas sessions are used for more secure
and temporary data.
"""

from flask import Flask, request, make_response

app = Flask(__name)

# Set a cookie with the key 'username' and value 'john_doe'
@app.route('/set_cookie')
def set_cookie():
    response = make_response('Cookie has been set')
    response.set_cookie('username', 'john_doe', max_age=3600)
    return response


# Get the value of the 'username' cookie
@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username')
    return f'The value of the cookie is: {username}'


# Delete the 'username' cookie
@app.route('/delete_cookie')
def delete_cookie():
    response = make_response('Cookie has been deleted')
    response.delete_cookie('username')
    return response


if __name__ == '__main__':
    app.run(debug=True)