from app import app
from flask import request
import os, requests, json
import base64

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

@app.route('/client-token')
def get_client_token():

    access_token = get_access_token()

    url = f'{os.environ.get("PAYPAL_BASE")}/v1/identity/generate-token'
    
    headers = {
        "Authorization": f'Bearer {access_token}',
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers)

    return response.json()['client_token'], response.status_code

@app.route('/auth-assertion-value')
def get_auth_assertion_value():

    client_id = os.environ.get('PAYPAL_CLIENT_ID')
    seller_id = os.environ.get('PAYPAL_ACCT_ID')
    seller_email = os.environ.get('PAYPAL_ACCT_EMAIL')

    header = {
        "alg": "none"
    }

    payload = {
        "iss": client_id,
        "payer_id": seller_id,
        # "payer_id": seller_email,
    }

    encodedHeader = base64.b64encode(json.dumps(header).encode('utf-8'))
    encodedPayload = base64.b64encode(json.dumps(payload).encode('utf-8'))

    return f'{encodedHeader}.{encodedPayload}.'

@app.route('/refund')
def refund_payment():

    auth_asssertion = get_auth_assertion_value()
    token = get_access_token()['access_token']
    capture_id = None

    url = f'{os.environ.get("PAYPAL_BASE")}/v2/payments/captures/{capture_id}/refund'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
        'PayPal-Request-Id': 't123',    # user-generated id; unique id for order between Paypal Account Manager and self
        # 'PayPal-Auth-Assertion': auth_asssertion  # required with merchant implementation, according to docs
    }

#  payload not required if it is full refund
    # payload = {
    #     'amount': {
    #         'value': '10.00',
    #         'currency_code': 'USD'
    #     }
    # }

    response = requests.post(url, headers=headers)
    # response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json(), response.status_code


@app.route('/api/orders', methods=['POST'])
def create_order():

    cart = {
        "amount": {
            "currency_code": "USD",
            "value": "10.00"
        },
        # "payee": {
        #     "email": "sb-nyblt29881484@business.example.com",
        #     "merchant_id": "EM2QT8H7XV3BU"
        # },
        # "payment_instruction": {
        #     "platform_fees": [
        #         {
        #             "amount": {
        #                 "value": "10.00",
        #                 "currency_code": "USD"
        #             }
        #         }
        #     ],
        # },
        # "disbursement_mode": "DELAYED",
    }
    token = get_access_token()['access_token']

    url = f'{os.environ.get("PAYPAL_BASE")}/v2/checkout/orders'
    payload = {
        "intent": "CAPTURE",
        "purchase_units": [cart],
    }

    # data = { 
    #     "intent": "CAPTURE",    # !required; capture payment immediately
    #     "purchase_units": [   # !required;
    #         { 
    #             "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",     # unique ID for purchase unit, for self-use, required if have multiple purchase units, `default` as default
    #             "description": "registration fee for ABC event",     # description
    #             "invoice_id": "abc-1" # unique ID of invoice from self business, for self-use
    #             "soft_descriptor": "EVENT REG" # description on payer statement, for payer, max 22 char
    #             "amount": {     # !required; payment detail
    #                 "currency_code": "USD",   # !required
    #                 "value": "100.00"     # !required
    #             },
    #             "payee": {
    #                 "email": "merchant@email.com",  # event organizer email address
    #                 "merchant_id": "5nz3d5f628a74"  # event organizer encrypted paypal account id
    #             },
    #            "payment_instruction": {
    #                 "platform_fees": [
    #                    {
    #                       "currency_code": "USD", 
    #                       "value": "10.00"
    #                    }
    #                ],
    #            "disbursement_mode": "DELAYED"
    #           },
    #        } 
    #     ],
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
        'PayPal-Request-Id': 'abc1',    # user-generated id; unique id for order between Paypal Account Manager and self
        'Authorization': f'Bearer {token}', # !required
        'Content-Type': 'application/json', # !required
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

    """ 
    Example for response.json() from PayPal on success capture order 

        { 
            'id': '9FV27953KK686364C', # order ID
            'status': 'COMPLETED', 
            'payment_source': {
                'paypal': {
                    'email_address': 'email@personal.example.com', 
                    'account_id': '4PTH5SLX8SB3J', 
                    'account_status': 'VERIFIED', 
                    'name': {'given_name': 'John', 'surname': 'Doe'}, 
                    'address': {'country_code': 'US'}
                }
            }, 
            'purchase_units': [
                {
                    'reference_id': 'default', 
                    'shipping': {
                        'name': {'full_name': 'John Doe'}, 
                        'address': {'address_line_1': '1 Main St', 'admin_area_2': 'San Jose', 'admin_area_1': 'CA', 'postal_code': '95131', 'country_code': 'US'}
                    }, 
                    'payments': {
                        'captures': [
                            {
                                'id': '9HN63998U9002144F',
                                'status': 'COMPLETED', 
                                'amount': {'currency_code': 'USD', 'value': '10.00'}, 
                                'final_capture': True, 
                                'seller_protection': {'status': 'ELIGIBLE', 'dispute_categories': ['ITEM_NOT_RECEIVED', 'UNAUTHORIZED_TRANSACTION']}, 
                                'seller_receivable_breakdown': {
                                    'gross_amount': {'currency_code': 'USD', 'value': '10.00'}, 
                                    'paypal_fee': {'currency_code': 'USD', 'value': '0.84'}, 
                                    'net_amount': {'currency_code': 'USD', 'value': '9.16'}
                                }, 
                                'links': [
                                    {
                                        'href': 'https://api.sandbox.paypal.com/v2/payments/captures/9HN63998U9002144F', 
                                        'rel': 'self', 'method': 'GET'
                                    }, 
                                    {
                                        'href': 'https://api.sandbox.paypal.com/v2/payments/captures/9HN63998U9002144F/refund', 
                                        'rel': 'refund', 'method': 'POST'
                                    }, 
                                    {
                                        'href': 'https://api.sandbox.paypal.com/v2/checkout/orders/9FV27953KK686364C', 
                                        'rel': 'up', 'method': 'GET'
                                    }
                                ], 
                                'create_time': '2024-06-25T19:29:29Z', 
                                'update_time': '2024-06-25T19:29:29Z'
                            }
                        ]
                    }
                }
            ], 
            'payer': {
                'name': {'given_name': 'John', 'surname': 'Doe'}, 
                'email_address': 'email@personal.example.com', 
                'payer_id': '4PTH5SLX8SB3J', 
                'address': {'country_code': 'US'}
            }, 
            'links': [{'href': 'https://api.sandbox.paypal.com/v2/checkout/orders/9FV27953KK686364C', 'rel': 'self', 'method': 'GET'}]
        }

    """

    return response.json(), response.status_code

# @staticmethod
# def parse_response(request_Body):


