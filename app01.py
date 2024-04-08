from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = {'message':'Hello,World!'}
    return jsonify(data)

@app.route('/mygunicorn/unix/')
def hello_gunicorn():
    data = {'message':'Hello,Gunicorn!'}
    return jsonify(data)

@app.route('/myuwsgi/unix/')
def hello_uwsgi():
    data = {'message':'Hello,uWSGI!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

