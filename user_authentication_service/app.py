#!/usr/bin/env python3
"""Application file"""
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_jsnofiy():
    return jsonify(request.data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
