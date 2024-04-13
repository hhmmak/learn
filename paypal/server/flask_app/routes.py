from app import app
from flask import request
import os, requests, json

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

@app.route('/api/orders', methods=['POST'])
def create_order():

    cart = {
                "reference_id": "cba1",
                "amount": {
                    "currency_code": "USD",
                    "value": "100.00"
                }
            }
    token = get_access_token()['access_token']

    url = f'{os.environ.get("PAYPAL_BASE")}/v2/checkout/orders'
    payload = {
        "intent": "CAPTURE",
        "purchase_units": [cart],
    }

    # data = { 
    #     "intent": "CAPTURE",    # capture payment immediately
    #     "purchase_units": [ 
    #         { 
    #             "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",     # guild-set reference id
    #             "amount": {     # payment detail
    #                 "currency_code": "USD", 
    #                 "value": "100.00" 
    #             },
    #             "payee": {
    #                 "email": "merchant@email.com",  # event organizer email address
    #                 "merchant_id": "5nz3d5f628a74"  # event organizer encrypted paypal account id
    #             }
    #         } 
    #     ],
    #     "payment_instruction": {
    #         "platform_fees": [
    #             {
    #                 "currency_code": "USD", 
    #                 "value": "10.00"
    #             }
    #         ],
    #         "disbursement_mode": "DELAYED"
    #     },
    #     "payment_source": { 
    #         "paypal": { 
    #             "experience_context": { 
    #                 "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED", 
    #                 "brand_name": "EXAMPLE INC", 
    #                 "locale": "en-US", 
    #                 "landing_page": "LOGIN", 
    #                 "shipping_preference": "SET_PROVIDED_ADDRESS",
    #                 "user_action": "PAY_NOW",
    #                 "return_url": "https://example.com/returnUrl",
    #                 "cancel_url": "https://example.com/cancelUrl" 
    #             } 
                
    #         } 
    #     }
    # }

    headers = {
        'Content-Type': 'application/json',
        'PayPal-Request-Id': 'abc1',
        'Authorization': f'Bearer {token}',
        # Uncomment one of these to force an error for negative testing (in sandbox mode only). Documentation:
        # https://developer.paypal.com/tools/sandbox/negative-testing/request-headers/
        # "PayPal-Mock-Response": '{"mock_application_codes": "MISSING_REQUIRED_PARAMETER"}'
        # "PayPal-Mock-Response": '{"mock_application_codes": "PERMISSION_DENIED"}'
        # "PayPal-Mock-Response": '{"mock_application_codes": "INTERNAL_SERVER_ERROR"}'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    return response.json(), response.status_code

@app.route('/api/orders/<order_id>', methods=['GET','POST'])
def order_details(order_id):

    token = get_access_token()['access_token']

    url = f'{os.environ.get("PAYPAL_BASE")}/v2/checkout/orders/{order_id}'

    print(url)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
        # Uncomment one of these to force an error for negative testing (in sandbox mode only). Documentation:
        # https://developer.paypal.com/tools/sandbox/negative-testing/request-headers/
        # "PayPal-Mock-Response": '{"mock_application_codes": "MISSING_REQUIRED_PARAMETER"}'
        # "PayPal-Mock-Response": '{"mock_application_codes": "PERMISSION_DENIED"}'
        # "PayPal-Mock-Response": '{"mock_application_codes": "INTERNAL_SERVER_ERROR"}'
    }

    response = requests.get(url, headers=headers)

    return response.json(), response.status_code

@app.route('/api/orders/<order_id>/capture', methods=['POST'])
def capture_order(order_id):

    token = get_access_token()['access_token']

    url = f'{os.environ.get("PAYPAL_BASE")}/v2/checkout/orders/{order_id}/capture'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
        # Uncomment one of these to force an error for negative testing (in sandbox mode only). Documentation:
        # https://developer.paypal.com/tools/sandbox/negative-testing/request-headers/
        # "PayPal-Mock-Response": '{"mock_application_codes": "MISSING_REQUIRED_PARAMETER"}'
        # "PayPal-Mock-Response": '{"mock_application_codes": "PERMISSION_DENIED"}'
        # "PayPal-Mock-Response": '{"mock_application_codes": "INTERNAL_SERVER_ERROR"}'
    }

    response = requests.post(url, headers=headers)

    return response.json(), response.status_code

# @staticmethod
# def parse_response(request_Body):
