from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()
api = Api(app, prefix='/api/v1')

users = {
    'admin': 'adminpassword'
}

@auth.verify_password
def verify_password(username, password):
    if username in users and password and users[username] == password:
        return True
    return False


class PrivateResource(Resource):
    @auth.login_required
    def get(self):
        return {'message': 'Hello, private world!'}


api.add_resource(PrivateResource, '/private')

if __name__ == '__main__':
    app.run(debug=True)