from functools import wraps
from flask import jsonify, request

check_auth = lambda username, password: username == 'admin' and password == 'admin'

def login_required(func):
    @wraps(func)
    def authentication(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({'message': 'Authentication required'}), 401
        return func(*args, **kwargs)
    return authentication
