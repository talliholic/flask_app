from flask import Flask

app = Flask(__name__)

@app.route("/read", methods=["GET"])
def read_user():           
    return "Flask app running"
