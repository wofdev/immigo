from rest_framework.test import RequestsClient

# here we check if we get 200 status code from our api and also if number of news is 5 for Api test

import json
client = RequestsClient()
response = client.get('http://127.0.0.1:8000/')
assert response.status_code == 200
assert len(json.loads(response.content)) == 5
