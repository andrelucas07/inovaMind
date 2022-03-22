from flask import Flask, make_response, jsonify, request
import requests
import json
import logging

app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.INFO, format=f'%(asctime)s : %(message)s')

@app.route('/listar', methods=['GET'], )
def listar():

    limit = request.args.get('limit', 5)
    
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)

    if response.status_code == 404:
        response_404 = {"error": {"reason": "Usuários não econtrados"}}
        app.logger.warning(jsonify(response_404))
        return make_response(jsonify(response_404))
    
    if not response.status_code == 200:
        response_others = {"error": {"reason": "Ocorreu um erro"}}
        app.logger.warning(jsonify(response_others), response.status_code)
        return make_response(jsonify(response_others), response.status_code)

    users = json.loads(response.content)[:int(limit)]
    normalized_users = []

    for user in users:
        user = {
            'id': user['id'],
            'title': user['title']
        }
        normalized_users.append(user)

    app.logger.info('Response: ' + json.dumps(normalized_users))

    return jsonify(normalized_users)
