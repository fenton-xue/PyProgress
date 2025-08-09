from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return {"code": 0, "msg": "success", "data": "hello world"}


if __name__ == '__main__':
    app.run(debug=True)