from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=5550, debug=True)
    app.run(debug=False, host='0.0.0.0', port=5000)
