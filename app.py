from flask import Flask , request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/classify', methods=['POST'])
def classify():
    error = None
    return {
        "text": request.json['text'],
        "type": 5,
    }


if __name__ == '__main__':
    app.run()
