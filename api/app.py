from flask import Flask, jsonify, request
import requests
import json
import logging
import basic_auth
from utility import normalized_details

app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.INFO, format=f'%(asctime)s : %(message)s')

@app.route('/listar', methods=['GET'], )
@basic_auth.login_required
def listar():
    limit = request.args.get('limit', 5)
    
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    try:
        details = json.loads(response.content)[:int(limit)]
        
        normalized_details(details)

        app.logger.info('Response: ' + json.dumps(normalized_details(details)))

        return jsonify(normalized_details(details))
    
    except ValueError:
        return jsonify({
                    "error": {
                    "reason": "Filtro inválido ou valor do filtro não numérico.",
                    }
                }), 404
