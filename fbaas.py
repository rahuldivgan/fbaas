from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/loaderio-cef9f1fd6b0734d29b0a59a28ccfa7f4/')
def loader():
    return 'loaderio-cef9f1fd6b0734d29b0a59a28ccfa7f4'

@app.route('/fizz/<num>')
def api_fizz(num):
    num = int(num)
    if num < 0 or num > 501:
        return jsonify(error="Out of bounds"), 400
    elif num%3 == 0:
        return jsonify(value="Fizz")
    else:
        return jsonify(error="Not divisible by 3"), 404

@app.route('/buzz/<num>')
def api_buzz(num):
    num = int(num)
    if num < 0 or num > 501:
        return jsonify(error="Out of bounds"), 400
    elif num%5 == 0:
        return jsonify(value="Buzz")
    else:
        return jsonify(error="Not divisible by 5"), 404

@app.route('/fizzbuzz/<num>')
def api_fizzbuzz(num):
    num = int(num)
    if num < 0 or num > 1001:
        return jsonify(error="Out of bounds"), 400
    elif num%15 == 0:
        return jsonify(value="FizzBuzz")
    elif num%5 == 0:
        return jsonify(value="Buzz")
    elif num%3 == 0:
        return jsonify(value="Fizz")
    else:
        return jsonify(error="Not divisible by 3 or 5"), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
