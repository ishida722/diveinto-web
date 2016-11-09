from flask import Flask

app = Flask(__name__)

message = 'hello world'

@app.route('/')
def hello():
    return message

@app.route('/message')
def messaging():
    message = 'text'
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0')
