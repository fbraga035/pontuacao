from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Bubble!'

@app.route('/api/exemplo', methods=['GET'])
def exemplo():
    data = {'mensagem': 'Esta é uma resposta da API Python'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
