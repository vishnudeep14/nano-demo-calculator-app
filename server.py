from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world",200

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    print(data)
    if 'first' in data and 'second' in data:
        first = data['first']
        second = data['second']
        result = first + second
        return jsonify({'result of summation': result}),200
    else:
        return jsonify({'error': 'Invalid data'}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    if 'first' in data and 'second' in data:
        num1 = data['first']
        num2 = data['second']
        result = num1 - num2
        return jsonify({'result in subtraction': result}),200
    else:
        return jsonify({'error': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
