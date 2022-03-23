
def normalized_details(details):
    normalized_details = []

    for data in details:
        data = {
            'id': data['id'],
            'title': data['title']
        }
        normalized_details.append(data)

    return normalized_details