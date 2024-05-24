#!/usr/bin/env python3
"""
Code to run web templateon flask with port 0.0.0.0:5000
"""


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_w():
    return ""<p>Hello, World</p>

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
