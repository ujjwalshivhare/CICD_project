from flask import Flask

app = Flask(__name__)


@app.route("/info")
def usinfo():
    return "i am from india"


@app.route("/phone")
def usphone():
    return "12345678"


#to connect to the world
app.run(host="0.0.0.0")
