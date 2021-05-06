from flask import Flask

from api import Wiki
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/wiki/<lang>/<title>', methods=['GET'])
def wiki(lang, title):
    return Wiki().read(title)


if __name__ == '__main__':
    app.run()
