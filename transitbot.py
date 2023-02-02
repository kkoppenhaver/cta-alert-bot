from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/listen', methods=['POST'])
def hello(name=None):
    data = request.json
    return jsonify(data)

