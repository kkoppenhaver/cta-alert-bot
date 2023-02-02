from flask import Flask, request, jsonify

import json
import os
from dotenv import load_dotenv

from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

load_dotenv()

PUBLIC_KEY = os.getenv('APP_PUBLIC_KEY')

app = Flask(__name__)

@app.route('/listen', methods=['POST'])
def hello(name=None):
    # verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    # signature = request.headers["X-Signature-Ed25519"]
    # timestamp = request.headers["X-Signature-Timestamp"]
    body = request.data.decode("utf-8")

    # return body

    # try:
    #     verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
    # except BadSignatureError:
    #     abort(401, 'invalid request signature')

    if request.json["type"] == 1:
        return jsonify({
            "type": 1
        })
    else:

        parsed_body = json.loads(body)
        parsed_body = parsed_body['data']['options']
        
        return jsonify({
            "type": 4,
            "data": {
                "tts": False,
                "content": json.dumps(parsed_body),
                "embeds": [],
                "allowed_mentions": { "parse": [] }
            }
        })

    # try:
        # body = request.json
            
        # signature = request.headers.get('x-signature-ed25519')
        # timestamp = request.headers.get('x-signature-timestamp')

        # # validate the interaction

        # verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

        # message = timestamp + body
        
        # try:
        #   verify_key.verify(message.encode(), signature=bytes.fromhex(signature))
        # except BadSignatureError:
        #   return jsonify('invalid request signature'), 401

        
        # handle the interaction

    #     t = body['type']

    #     if t == 1:
    #       return jsonify({type: 1}), 200
    #     elif t == 2:
    #       return jsonify({type: 2}), 200
    #     else:
    #         return jsonify('unhandled request type'), 400
    # except:
    #     raise

# def command_handler(body):
#     command = body['data']['name']

#     if command == 'bleb':
#         return {
#           'statusCode': 200,
#           'body': json.dumps({
#             'type': 4,
#             'data': {
#               'content': 'Hello, World.',
#             }
#           })
#         }
#     else:
#         return {
#           'statusCode': 400,
#           'body': json.dumps('unhandled command')
#         }

