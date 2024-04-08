from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(ssl_context=('certificate.crt', 'private.key'), host='0.0.0.0', port=443)

