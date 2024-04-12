from flask import jsonify, request
from app import app
import os, base64, requests

# Home route
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def hello_world_test():
    return 'Hello, World! Test'



# get access token from paypal
@app.route('/access-token')
def get_access_token():

    client_id = os.environ.get('PAYPAL_CLIENT_ID')
    client_secret = os.environ.get('PAYPAL_CLIENT_SECRET')

    if not client_id or not client_secret:
        return "No client_id"

    headers = {
        'Content-Type': 'application/json',
    }

    data = 'grant_type=client_credentials'

    response = requests.post(
        f'{os.environ.get("PAYPAL_BASE")}/v1/oauth2/token', auth=(client_id,client_secret), headers=headers, data=data)

    return response.json()
