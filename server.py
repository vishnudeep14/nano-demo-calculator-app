from flask import Flask, request, jsonify
import requests
app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello Word",200

@app.route("/calculator/add", methods=['POST'])
def add():
    data=request.json
    if "first" in data and 'second' in data:
        first=data['first']
        second=data['second']
        res=first+second
        return jsonify({'result-of-the-summation:',res}),200
    else:
        return jsonify({'error': 'Invalid data'}), 400
   
@app.route("/calculator/sub", methods=['POST'])
def subtract():
    data=request.json
    if "first" in data and 'second' in data:
        first=data['first']
        second=data['second']
        res=first-second
        return jsonify({'result-of-the-subtraction',res}),200
    else:
        return jsonify({'error': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
