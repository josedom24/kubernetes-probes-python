from time import sleep
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hola, mundo</h1>"

@app.route("/healthz")
def healthz():
    sllep(2)
    return "ok"

@app.route("/ready")
def ready():
    sleep(5)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
