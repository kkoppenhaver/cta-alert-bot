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
    try:
        body = request.json
            
        signature = request.headers.get('x-signature-ed25519')
        timestamp = request.headers.get('x-signature-timestamp')

        # validate the interaction

        verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

        message = timestamp + json.dumps(body, separators=(',', ':'))
        
        try:
          verify_key.verify(message.encode(), signature=bytes.fromhex(signature))
        except BadSignatureError:
          return {
            'statusCode': 401,
            'body': json.dumps('invalid request signature')
          }
        
        # handle the interaction

        t = body['type']

        if t == 1:
          return {
            'statusCode': 200,
            'body': json.dumps({
              'type': 1
            })
          }
        elif t == 2:
          return command_handler(body)
        else:
          return {
            'statusCode': 400,
            'body': json.dumps('unhandled request type')
          }
    except:
        raise

def command_handler(body):
    command = body['data']['name']

    if command == 'bleb':
        return {
          'statusCode': 200,
          'body': json.dumps({
            'type': 4,
            'data': {
              'content': 'Hello, World.',
            }
          })
        }
    else:
        return {
          'statusCode': 400,
          'body': json.dumps('unhandled command')
        }

