from flask import Flask, jsonify, request, abort, Blueprint, make_response

import login_service
from authentication_exception import AuthenticationException
from user import User

app = Flask(__name__)
login_controller = Blueprint('login_controller', __name__)


@login_controller.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        if not username or not password:
            abort(400)

        user = User(username, password)
        login_service.authenticate(user)

        return jsonify(user.to_dict()), 200

    except AuthenticationException as e:
        return make_response(jsonify({'message': str(e)}), 400)

    except:
        return jsonify({'message': 'Invalid username/password'}), 400
