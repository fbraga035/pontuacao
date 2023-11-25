from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    # Use o Waitress para servir o aplicativo
    serve(app, host="0.0.0.0", port=5000)
