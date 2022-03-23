from flask import jsonify

def normalized_details(details):
    normalized_details = []

    for data in details:
        data = {
            'id': data['id'],
            'title': data['title']
        }
        normalized_details.append(data)

    return normalized_details

def validate_limit(limit):
    if limit is None:
        return jsonify({
                    "error": {
                    "reason": "Invalid filter or ivalid value",
                    }
                }), 500
    else:
        pass
