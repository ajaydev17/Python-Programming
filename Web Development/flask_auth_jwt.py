from flask import Flask, request, jsonify, make_response
import jwt
import datetime
import functools

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'


def token_required(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated


@app.route('/unprotected')
def unprotected_route():
    return 'This route is not protected by authentication.'


@app.route('/protected')
@token_required
def protected_route():
    return 'This route is protected by authentication.'


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'admin' and data['password'] == 'admin':
        token = jwt.encode(
            {
                'user': data['username'],
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
            },
            app.config['SECRET_KEY']
        )
        return jsonify({'token': token.decode('UTF-8')})

    return make_response(
        'Could not verify',
        401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )


if __name__ == '__main__':
    app.run(debug=True)
