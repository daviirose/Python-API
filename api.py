from flask import Flask, jsonify, request #Imports objects from the Flask model
app = Flask(__name__)

languages = [{'name' : 'Javascript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})

    if __name__ == '__main__':
        app.run(debug=True, port=8080) #Runs app on port 8080 in debug mode
