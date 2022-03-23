from flask import Flask, jsonify, request
import requests
import json
import logging
import basic_auth
from utility import normalized_details, validate_limit

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
                    "error": {
                    "reason": "Route not found.",
                    }
                }), 404

logging.basicConfig(filename='record.log', level=logging.INFO, format=f'%(asctime)s : %(message)s')

@app.route('/listar', methods=['GET'], )
@basic_auth.login_required
def listar():
    limit = request.args.get('limit', 5)
    
    validate_limit(limit)

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
                    "reason": "Invalid filter or ivalid value",
                    }
                }), 500
