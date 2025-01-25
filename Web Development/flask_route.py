"""
Routing in Flask is the process of mapping URLs to specific functions within 
the application, allowing the server to respond to different URLs with 
appropriate content. Flask provides a @app.route decorator that is used to specify 
which function should handle each route. By defining routes, developers can create 
different pages or actions that correspond to different URL paths.
Routes are defined by the developer and can contain dynamic segments that allow for
variable data in URLs, such as /<username>.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to the home page!'


@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'
    

if __name__ == '__main__':
    app.run(debug=True)