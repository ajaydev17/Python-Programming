"""
SQLAlchemy is a popular Object Relational Mapper (ORM) for Python that simplifies
interactions with databases by allowing developers to work with Python objects instead of
writing raw SQL queries. When used with Flask, SQLAlchemy enables easy database
connection, object-oriented data management, and query generation.
Flask-SQLAlchemy is an extension that integrates SQLAlchemy with Flask, providing a
straightforward way to configure and use a database in Flask applications.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f'<Student {self.name}>'


if __name__ == '__main__':
    db.create_all()  # Create the database tables if they don't exist
    app.run(debug=True)