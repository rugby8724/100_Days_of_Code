from flask import Flask
app = Flask(__name__)

@app.rouge('/')
def hello_world():
    return 'Hello, World'