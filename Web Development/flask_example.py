"""
Flask is a lightweight web framework written in Python, designed to be simple and
easy to extend. It is widely used for developing web applications due to its flexibility and
simplicity. Flask is considered a micro-framework, which means it provides the core
functionality needed to get a web app up and running, but it leaves out more complex
components, such as form validation and database abstraction layers, which can be added as
required.
Flask uses a simple design that allows developers to easily create routes, define request
handling functions, and render templates. Flask’s minimalistic approach makes it easy to
learn and an ideal choice for small to medium-sized applications or as a base framework that
can be extended.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
