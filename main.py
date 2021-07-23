from flask import Flask, json, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")

# def index():
#     return "index"

def index():
    return jsonify({
        "data": data,
        "message": "success"
    }, 200)

@app.route("/star")

def getData():
    name = request.args.get("name")
    starData = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": starData,
        "message": "success"
    })

if __name__ == "__main__":
    app.run()