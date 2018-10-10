from flask import Flask, jsonify, request #Imports objects from the Flask model
app = Flask(__name__)

languages = [{'name' : 'Javascript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    lang = [language for language in languages if language['name'] == name]
    return jsonify({'language' : lang[0]})

@app.route('/lang', methods=['POST'])
def addOne():
    language = {'name' : request.json['name']}

    languages.append(language)
    return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
    lang = [language for language in languages if language['name'] == name]
    lang[0]['names'] = request.json['name']
    return jsonify({'language' : lang[0]})

@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
    lang = [language for language in languages if language['name'] == name]
    langauge.remove(lang[0])
    return jsonify({'languages' : languages})

if __name__ == '__main__':
    app.run(debug=True, port=8080) #Runs app on port 8080 in debug mode
